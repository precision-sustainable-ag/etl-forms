import pandas as pd
import sys
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
import sqlalchemy
import traceback
import logging
import time
import datetime
from pytz import timezone

from .tables import shadow_table_info

class ProductionPusher:
    def __init__(self, mode=None):
        load_dotenv()

        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        print("Starting to push to prod")
        print(loc_dt)

        self.create_loggers()
        # print("connected to dbs")

        self.shadow_table_info = shadow_table_info.info

        self.mode = mode

        if self.mode == "live":
            print("live")
            self.connect_to_shadow_live()
            self.connect_to_prod_live()
        elif self.mode == "local" or self.mode == None:
            print("local")
            self.connect_to_shadow_local()
            self.connect_to_prod_local()

        self.encountered_unicity_error = 0
        self.encountered_no_rows_error = 0
        self.encountered_not_pushed_error = 0
        self.encountered_general_error = 0

    def connect_to_shadow_local(self):
        postgres_host = os.environ.get('LOCAL_SHADOW_HOST')
        postgres_dbname = os.environ.get('LOCAL_SHADOW_DBNAME')
        postgres_user = os.environ.get('LOCAL_SHADOW_USER')
        postgres_password = os.environ.get('LOCAL_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('LOCAL_SHADOW_SSLMODE')
        postgres_port = os.environ.get('LOCAL_SHADOW_PORT')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        # print(postgres_con_string)
        self.shadow_con = psycopg2.connect(postgres_con_string)
        self.shadow_cur = self.shadow_con.cursor()
        self.shadow_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(postgres_engine_string)

        print("connected to shadow local")

    def connect_to_shadow_live(self):
        postgres_host = os.environ.get('LIVE_SHADOW_HOST')
        postgres_dbname = os.environ.get('LIVE_SHADOW_DBNAME')
        postgres_user = os.environ.get('LIVE_SHADOW_USER')
        postgres_password = os.environ.get('LIVE_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('LIVE_SHADOW_SSLMODE')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        # print(postgres_con_string)
        self.shadow_con = psycopg2.connect(postgres_con_string)
        self.shadow_cur = self.shadow_con.cursor()
        self.shadow_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(postgres_engine_string)

        print("connected to shadow live")

    def connect_to_prod_local(self):
        postgres_host = os.environ.get('LOCAL_PROD_HOST')
        postgres_dbname = os.environ.get('LOCAL_PROD_DBNAME')
        postgres_user = os.environ.get('LOCAL_PROD_USER')
        postgres_password = os.environ.get('LOCAL_PROD_PASSWORD')
        postgres_sslmode = os.environ.get('LOCAL_PROD_SSLMODE')
        postgres_port = os.environ.get('LOCAL_PROD_PORT')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        # print(postgres_con_string)
        self.local_con = psycopg2.connect(postgres_con_string)
        self.local_cur = self.local_con.cursor()
        self.local_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        self.local_engine = sqlalchemy.create_engine(postgres_engine_string)

        print("connected to prod local")

    def connect_to_prod_live(self):
        postgres_host = os.environ.get('LIVE_PROD_HOST')
        postgres_dbname = os.environ.get('LIVE_PROD_DBNAME')
        postgres_user = os.environ.get('LIVE_PROD_USER')
        postgres_password = os.environ.get('LIVE_PROD_PASSWORD')
        postgres_sslmode = os.environ.get('LIVE_PROD_SSLMODE')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        self.local_con = psycopg2.connect(postgres_con_string)
        self.local_cur = self.local_con.cursor()
        self.local_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.local_engine = sqlalchemy.create_engine(postgres_engine_string)

        print("connected to prod live")

    def close_cons(self):
        self.shadow_con.close()
        self.local_con.close()

    def setup_logger(self, name, log_file, level=logging.INFO):
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler = logging.FileHandler(log_file)        
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
    
    def create_loggers(self):
        self.successful_logger = self.setup_logger('successful_logger', './logs/successful.log')
        self.failed_unicity_constraint_logger = self.setup_logger('failed_unicity_constraint_logger', './logs/failed_unicity_constraint.log')
        self.no_rows_affected_logger = self.setup_logger('no_rows_affected_logger', './logs/no_rows_affected.log')
        self.not_inserted_into_not_pushed_to_prod = self.setup_logger('not_inserted_into_not_pushed_to_prod', './logs/not_inserted_into_not_pushed_to_prod.log')
        self.general_error_logger = self.setup_logger('general_error_logger', './logs/general_error.log')

    def update_failed_rows(self, table_name, failing_sid, rawuid):
        insert_query = "INSERT INTO not_pushed_to_prod (table_name, failing_sid, rawuid) VALUES ({values})"
        insert_query = sql.SQL(insert_query).format(
            values = sql.SQL(', ').join(sql.Placeholder() * 3)
        )

        try:
            self.shadow_cur.execute(insert_query, [table_name, failing_sid, rawuid])
            self.shadow_con.commit()
        except Exception:
            self.not_inserted_into_not_pushed_to_prod.error(table_name + "\n" + str(failing_sid) + "\n" + str(rawuid) + "\n")
            self.encountered_not_pushed_error += 1

    def try_queries(self, shadow_query, prod_query, prod_values, sid, raw_uid, prod_table_name, table_name):
        try:
            self.local_cur.execute(prod_query, prod_values)
            if self.local_cur.rowcount == 0:
                self.no_rows_affected_logger.error("\n" + prod_query.as_string(self.local_con) + "\n" + str(prod_values) + "\n" + table_name + "\nsid: " + str(sid) + " raw_uid: " + str(raw_uid) + "\n")
                self.update_failed_rows(table_name, sid, raw_uid)
                self.encountered_no_rows_error += 1
                return
            self.local_con.commit()
            self.shadow_cur.execute(shadow_query, [sid])
            self.shadow_con.commit()
            self.successful_logger.info("\n" + prod_query.as_string(self.local_con) + "\n" + str(prod_values) + "\n" + table_name + "\nsid: " + str(sid) + " raw_uid: " + str(raw_uid) + "\n")
        except psycopg2.errors.UniqueViolation:
            self.failed_unicity_constraint_logger.error("\n" + prod_query.as_string(self.local_con) + "\n" + str(prod_values) + "\n" + table_name + "\nsid: " + str(sid) + " raw_uid: " + str(raw_uid) + "\n")
            self.shadow_cur.execute(shadow_query, [sid])
            self.shadow_con.commit()
            self.encountered_unicity_error += 1
        except Exception:
            self.general_error_logger.error("\n" + prod_query.as_string(self.local_con) + "\n" + str(prod_values) + "\n" + table_name + "\nsid: " + str(sid) + " raw_uid: " + str(raw_uid) + "\n")
            self.general_error_logger.error(str(traceback.print_exc(file=sys.stdout)) + "\n")
            self.encountered_general_error += 1

    def insert_row(self, values_from_table, all_rows, prod_table_name, table_name):
        rows_list = []
        for value in all_rows:
            rows_list.append(sql.Identifier(value))

        unpushed_rows = pd.DataFrame(pd.read_sql("SELECT * FROM {} WHERE pushed_to_prod = 0".format(table_name), self.shadow_engine))

        for index, row_entry in unpushed_rows.iterrows():
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
                table=sql.Identifier(table_name),
                sid = sql.Placeholder()
            )

            self.try_queries(update_query, insert_query, values_list, row_entry.get("sid"), raw_uid, prod_table_name, table_name)

    def generate_update_prod_sql(self, values_dict, unique_dict, prod_table_name):
        identifiers_list = []
        # creates list of sql statements (var1 = %{} AND var2 = ${} ...etc)
        for i, (k, v) in enumerate(unique_dict.items()):
            if i == len(unique_dict)-1:
                identifiers_list.append(sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]))
            else:
                identifiers_list.append(sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k), sql.SQL(" AND ")])) 

        null_vals_list = []
        # creates list of sql statements (var1 IS NULL AND var2 IS NULL ...etc)
        for i, (k, v) in enumerate(values_dict.items()):
            if i == len(values_dict)-1:
                null_vals_list.append(sql.Composed([sql.Identifier(k), sql.SQL(" IS NULL ")]))
            else:
                null_vals_list.append(sql.Composed([sql.Identifier(k), sql.SQL(" IS NULL "), sql.SQL("AND ")]))      

        update_prod_query = sql.SQL("UPDATE {table} SET {values} WHERE {identifiers} AND {is_null_vals}").format(
            table=sql.Identifier(prod_table_name),
            values=sql.SQL(', ').join(
                sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]) for k in values_dict.keys()
            ),
            identifiers=sql.SQL('').join(
                identifiers_list
            ),
            is_null_vals=sql.SQL('').join(
                null_vals_list
            ),
        )

        return update_prod_query

    def update_row(self, values_from_table, all_rows, prod_table_name, table_name, unique_cols):
        rows_list = []
        for value in values_from_table:
            rows_list.append(sql.Identifier(value))

        unpushed_rows = pd.DataFrame(pd.read_sql("SELECT * FROM {} WHERE pushed_to_prod = 0".format(table_name), self.shadow_engine))

        for index, row_entry in unpushed_rows.iterrows():
            # print("\n")
            raw_uid = row_entry.get("rawuid")
            values_dict = {}
            for value in values_from_table:
                data = row_entry.get(value)
                values_dict[value] = data

            unique_dict = {}
            for value in unique_cols:
                data = row_entry.get(value)
                unique_dict[value] = data

            update_prod_query = self.generate_update_prod_sql(values_dict, unique_dict, prod_table_name)

            update_sql_string = "UPDATE {table} SET pushed_to_prod = 1 WHERE sid = {sid}"
            update_local_query = sql.SQL(update_sql_string).format(
                table=sql.Identifier(table_name),
                sid = sql.Placeholder()
            )

            values_dict.update(unique_dict)

            self.try_queries(update_local_query, update_prod_query, values_dict, row_entry.get("sid"), raw_uid, prod_table_name, table_name)

    def push_to_prod(self):
        for table_name, info in self.shadow_table_info.items():
            prod_table_name = table_name.split("__")[0]

            values_from_table = info.get("values_from_table")
            all_rows = info.get("all_rows")
            unique_cols = info.get("unique_cols")
            mode = info.get("mode")

            if mode == "insert":
                self.insert_row(values_from_table, all_rows, prod_table_name, table_name)

            elif mode == "update":
                self.update_row(values_from_table, all_rows, prod_table_name, table_name, unique_cols)
                
        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        print("Finished pushing to prod")
        print(loc_dt)

        self.encountered_unicity_error = 0
        self.encountered_no_rows_error = 0
        self.encountered_not_pushed_error = 0
        self.encountered_general_error = 0

        # print("Encountered {} unicity errors, {} no rows updated errors, {} not pushed errors, {} general errors".format())

        if self.encountered_unicity_error > 0 or self.encountered_no_rows_error > 0 or self.encountered_not_pushed_error > 0 or self.encountered_general_error:
            print("Encountered {} unicity errors,\n {} no rows updated errors,\n {} not pushed errors,\n {} general errors\n"\
                .format(self.encountered_unicity_error, self.encountered_no_rows_error, self.encountered_not_pushed_error, self.encountered_general_error))
# try:
#     mode = None
#     uid = None
#     if len(sys.argv) > 1:
#         mode = sys.argv[1]  

#     pp = ProductionPusher(mode)

#     # pp.push_to_prod()
#     pp.close_cons()

# except Exception:
#     print("an error ocurred \n")
#     print(traceback.print_exc(file=sys.stdout))

# pp = ProductionPusher()
# pp.push_to_prod()
# pp.close_cons()
