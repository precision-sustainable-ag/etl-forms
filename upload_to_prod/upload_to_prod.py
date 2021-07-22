import json
import pandas as pd
import re
import sqlite3
import sys
import time
import datetime
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import sqlalchemy
import mysql.connector
from pytz import timezone
import traceback

import tables.prod_table_info
import tables.shadow_table_info

class ProductionPusher:
    def __init__(self):
        load_dotenv()
        self.connect_to_postgres_shadow()
        self.connect_to_postgres_local()
        print("connected to dbs")

        self.prod_table_info = tables.prod_table_info.info
        self.shadow_table_info = tables.shadow_table_info.info

    def connect_to_postgres_shadow(self):
        postgres_host = os.environ.get('POSTGRESQL_SHADOW_HOST')
        postgres_dbname = os.environ.get('POSTGRESQL_SHADOW_DBNAME')
        postgres_user = os.environ.get('POSTGRESQL_SHADOW_USER')
        postgres_password = os.environ.get('POSTGRESQL_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('POSTGRESQL_SHADOW_SSLMODE')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        self.shadow_con = psycopg2.connect(postgres_con_string)
        self.shadow_cur = self.shadow_con.cursor()
        self.shadow_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(postgres_engine_string)

    def connect_to_postgres_local(self):
        postgres_host = os.environ.get('POSTGRESQL_LOCAL_HOST')
        postgres_dbname = os.environ.get('POSTGRESQL_LOCAL_DBNAME')
        postgres_user = os.environ.get('POSTGRESQL_LOCAL_USER')
        postgres_password = os.environ.get('POSTGRESQL_LOCAL_PASSWORD')
        postgres_sslmode = os.environ.get('POSTGRESQL_LOCAL_SSLMODE')
        postgres_port = os.environ.get('POSTGRESQL_LOCAL_PORT')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        self.local_con = psycopg2.connect(postgres_con_string)
        self.local_cur = self.local_con.cursor()
        self.local_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.local_engine = sqlalchemy.create_engine(postgres_engine_string)

    def close_cons(self):
        self.shadow_con.close()
        self.local_con.close()

    def push_to_prod(self):
        for table, info in self.shadow_table_info.items():
            prod_table_name = table.split("__")[0]
            print(prod_table_name)

            values_from_table = info.get("values_from_table")
            all_rows = info.get("all_rows")
            unique_cols = info.get("unique_cols")
            mode = info.get("mode")
            unicity_constraint = info.get("unicity_constraint")

            if mode == "insert":
                rows_list = []
                for value in all_rows:
                    rows_list.append(sql.Identifier(value))

                unpushed_rows = pd.DataFrame(pd.read_sql("SELECT * FROM {} WHERE pushed_to_prod = 0".format(table), self.shadow_engine))

                for index, row_entry in unpushed_rows.iterrows():
                    # print(rows_list)
                    values_list = []
                    for value in all_rows:
                        data = row_entry.get(value)
                        print(data)
                        values_list.append(data)


                    # insert_sql_string = "INSERT INTO {table} ({fields}) VALUES ({values}) ON CONFLICT ON CONSTRAINT " + unicity_constraint +  " DO NOTHING"
                    insert_sql_string = "INSERT INTO {table} ({fields}) VALUES ({values})"
                    insert_query = sql.SQL(insert_sql_string).format(
                        table=sql.Identifier(prod_table_name),
                        fields=sql.SQL(',').join(rows_list),
                        values = sql.SQL(', ').join(sql.Placeholder() * len(values_list))
                    )

                    update_sql_string = "UPDATE {table} SET pushed_to_prod = 1 WHERE sid = {sid}"
                    update_query = sql.SQL(update_sql_string).format(
                        table=sql.Identifier(table),
                        sid = sql.Placeholder()
                    )

                    try:
                        self.local_cur.execute(insert_query, values_list)
                        self.local_con.commit()
                        self.shadow_cur.execute(update_query, [row_entry.get("sid")])
                        self.shadow_con.commit()
                    except psycopg2.errors.UniqueViolation:
                        print("row already exists \n")
                        print(traceback.print_exc(file=sys.stdout))
                        self.shadow_cur.execute(update_query, [row_entry.get("sid")])
                        self.shadow_con.commit()
                    except Exception:
                        print("a different error ocurred")
                        print(traceback.print_exc(file=sys.stdout))

            elif mode == "update":
                rows_list = []
                for value in values_from_table:
                    rows_list.append(sql.Identifier(value))

                unpushed_rows = pd.DataFrame(pd.read_sql("SELECT * FROM {} WHERE pushed_to_prod = 0".format(table), self.shadow_engine))

                for index, row_entry in unpushed_rows.iterrows():
                    # print(rows_list)
                    values_dict = {}
                    for value in values_from_table:
                        data = row_entry.get(value)
                        values_dict[value] = data

                    unique_dict = {}
                    for value in unique_cols:
                        data = row_entry.get(value)
                        unique_dict[value] = data

                    # print(values_dict)
                    # obj = (', ').join(
                    #         sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k), sql.SQL(" AND ")]) for k in unique_dict.keys()
                    #     )
                    obj = []
                    for i, (k, v) in enumerate(unique_dict.items()):
                        # obj.append([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k), sql.SQL(" AND ")] )
                        if i == len(unique_dict)-1:
                            obj.append(sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]))
                        else:
                            obj.append(sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k), sql.SQL(" AND ")]))

                    # print(obj)
                    

                    update_prod_query = sql.SQL("UPDATE {table} SET {values} WHERE {id}").format(
                        table=sql.Identifier(prod_table_name),
                        values=sql.SQL(', ').join(
                            sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]) for k in values_dict.keys()
                        ),
                        id=sql.SQL('').join(
                            obj
                        ),
                    )
                    # update_prod_query.

                    print(update_prod_query.as_string(self.local_con))
                    values_dict.update(unique_dict)
                    # print(values_dict)


                    # # insert_sql_string = "INSERT INTO {table} ({fields}) VALUES ({values}) ON CONFLICT ON CONSTRAINT " + unicity_constraint +  " DO NOTHING"
                    # insert_sql_string = "UPDATE {table} ({fields}) VALUES ({values})"
                    # insert_query = sql.SQL(insert_sql_string).format(
                    #     table=sql.Identifier(prod_table_name),
                    #     fields=sql.SQL(',').join(rows_list),
                    #     values = sql.SQL(', ').join(sql.Placeholder() * len(values_dict))
                    # )

                    update_sql_string = "UPDATE {table} SET pushed_to_prod = 1 WHERE sid = {sid}"
                    update_local_query = sql.SQL(update_sql_string).format(
                        table=sql.Identifier(table),
                        sid = sql.Placeholder()
                    )

                    try:
                        self.local_cur.execute(update_prod_query, values_dict)
                        self.local_con.commit()
                        self.shadow_cur.execute(update_local_query, [row_entry.get("sid")])
                        self.shadow_con.commit()
                    except psycopg2.errors.UniqueViolation:
                        print("row already exists \n")
                        print(traceback.print_exc(file=sys.stdout))
                        self.shadow_cur.execute(update_local_query, [row_entry.get("sid")])
                        self.shadow_con.commit()
                    except Exception:
                        print("a different error ocurred")
                        print(traceback.print_exc(file=sys.stdout))

            # self.local_con.commit()



pp = ProductionPusher()
pp.push_to_prod()
pp.close_cons()