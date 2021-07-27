import pandas as pd
import sys
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import sqlalchemy
import traceback

import tables.shadow_table_info

class ProductionPusher:
    def __init__(self):
        load_dotenv()
        self.connect_to_postgres_shadow()
        self.connect_to_postgres_local()
        print("connected to dbs")

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

    def try_queries(self, shadow_query, prod_query, prod_values, sid, raw_uid, prod_table_name):
        try:
            self.local_cur.execute(prod_query, prod_values)
            if self.local_cur.rowcount == 0:
                print("no rows affected")
            self.local_con.commit()
            self.shadow_cur.execute(shadow_query, [sid])
            self.shadow_con.commit()
            print("succsessfully pushed row {} for table {}".format(raw_uid, prod_table_name))
        except psycopg2.errors.UniqueViolation:
            print("could not push row {} for table {}, row already exists".format(raw_uid, prod_table_name))
            print(traceback.print_exc(file=sys.stdout))
            self.shadow_cur.execute(shadow_query, [sid])
            self.shadow_con.commit()
        except Exception:
            print("could not push row {} for table {}, a different error occured".format(raw_uid, prod_table_name))
            print(traceback.print_exc(file=sys.stdout))

    def insert_row(self, values_from_table, all_rows, prod_table_name, table):
        rows_list = []
        for value in all_rows:
            rows_list.append(sql.Identifier(value))

        unpushed_rows = pd.DataFrame(pd.read_sql("SELECT * FROM {} WHERE pushed_to_prod = 0".format(table), self.shadow_engine))

        for index, row_entry in unpushed_rows.iterrows():
            print("\n")
            raw_uid = row_entry.get("rawuid")
            values_list = []
            for value in all_rows:
                data = row_entry.get(value)
                values_list.append(data)


            insert_query = "INSERT INTO {table} ({fields}) VALUES ({values})"
            insert_query = sql.SQL(insert_query).format(
                table=sql.Identifier(prod_table_name),
                fields=sql.SQL(',').join(rows_list),
                values = sql.SQL(', ').join(sql.Placeholder() * len(values_list))
            )

            update_sql_string = "UPDATE {table} SET pushed_to_prod = 1 WHERE sid = {sid}"
            update_query = sql.SQL(update_sql_string).format(
                table=sql.Identifier(table),
                sid = sql.Placeholder()
            )

            print(insert_query.as_string(self.local_con))

            self.try_queries(update_query, insert_query, values_list, row_entry.get("sid"), raw_uid, prod_table_name)

    def update_row(self, values_from_table, all_rows, prod_table_name, table, unique_cols):
        rows_list = []
        for value in values_from_table:
            rows_list.append(sql.Identifier(value))

        unpushed_rows = pd.DataFrame(pd.read_sql("SELECT * FROM {} WHERE pushed_to_prod = 0".format(table), self.shadow_engine))

        for index, row_entry in unpushed_rows.iterrows():
            print("\n")
            raw_uid = row_entry.get("rawuid")
            values_dict = {}
            for value in values_from_table:
                data = row_entry.get(value)
                values_dict[value] = data

            unique_dict = {}
            for value in unique_cols:
                data = row_entry.get(value)
                unique_dict[value] = data

            obj = []
            for i, (k, v) in enumerate(unique_dict.items()):
                if i == len(unique_dict)-1:
                    obj.append(sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]))
                else:
                    obj.append(sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k), sql.SQL(" AND ")]))                    

            update_prod_query = sql.SQL("UPDATE {table} SET {values} WHERE {id}").format(
                table=sql.Identifier(prod_table_name),
                values=sql.SQL(', ').join(
                    sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]) for k in values_dict.keys()
                ),
                id=sql.SQL('').join(
                    obj
                ),
            )

            print(update_prod_query.as_string(self.local_con))
            values_dict.update(unique_dict)

            update_sql_string = "UPDATE {table} SET pushed_to_prod = 1 WHERE sid = {sid}"
            update_local_query = sql.SQL(update_sql_string).format(
                table=sql.Identifier(table),
                sid = sql.Placeholder()
            )

            self.try_queries(update_local_query, update_prod_query, values_dict, row_entry.get("sid"), raw_uid, prod_table_name)

    def push_to_prod(self):
        for table, info in self.shadow_table_info.items():
            prod_table_name = table.split("__")[0]

            values_from_table = info.get("values_from_table")
            all_rows = info.get("all_rows")
            unique_cols = info.get("unique_cols")
            mode = info.get("mode")

            if mode == "insert":
                self.insert_row(values_from_table, all_rows, prod_table_name, table)

            elif mode == "update":
                self.update_row(values_from_table, all_rows, prod_table_name, table, unique_cols)

pp = ProductionPusher()
pp.push_to_prod()
pp.close_cons()