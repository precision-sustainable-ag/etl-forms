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

        self.create_loggers()
        self.global_logger.info("Starting to push to prod")
        self.global_logger.info(loc_dt)

        # self.global_logger.info("connected to dbs")

        self.shadow_table_info = shadow_table_info.info

        self.mode = mode

        if self.mode == "live":
            self.global_logger.info("live")
            self.connect_to_shadow_live()
            self.connect_to_prod_live()
        elif self.mode == "local" or self.mode == None:
            self.global_logger.info("local")
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
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(
            postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        # self.global_logger.info(postgres_con_string)
        self.shadow_con = psycopg2.connect(postgres_con_string)
        self.shadow_cur = self.shadow_con.cursor()
        self.shadow_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
            postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(postgres_engine_string)

        self.global_logger.info("connected to shadow local")

    def connect_to_shadow_live(self):
        postgres_host = os.environ.get('LIVE_SHADOW_HOST')
        postgres_dbname = os.environ.get('LIVE_SHADOW_DBNAME')
        postgres_user = os.environ.get('LIVE_SHADOW_USER')
        postgres_password = os.environ.get('LIVE_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('LIVE_SHADOW_SSLMODE')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
            postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        # self.global_logger.info(postgres_con_string)
        self.shadow_con = psycopg2.connect(postgres_con_string)
        self.shadow_cur = self.shadow_con.cursor()
        self.shadow_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(
            postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(postgres_engine_string)

        self.global_logger.info("connected to shadow live")

    def connect_to_prod_local(self):
        postgres_host = os.environ.get('LOCAL_PROD_HOST')
        postgres_dbname = os.environ.get('LOCAL_PROD_DBNAME')
        postgres_user = os.environ.get('LOCAL_PROD_USER')
        postgres_password = os.environ.get('LOCAL_PROD_PASSWORD')
        postgres_sslmode = os.environ.get('LOCAL_PROD_SSLMODE')
        postgres_port = os.environ.get('LOCAL_PROD_PORT')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(
            postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        # self.global_logger.info(postgres_con_string)
        self.local_con = psycopg2.connect(postgres_con_string)
        self.local_cur = self.local_con.cursor()
        self.local_con.autocommit = True

        # postgres_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        # self.local_engine = sqlalchemy.create_engine(postgres_engine_string)

        self.global_logger.info("connected to prod local")

    def connect_to_prod_live(self):
        postgres_host = os.environ.get('LIVE_PROD_HOST')
        postgres_dbname = os.environ.get('LIVE_PROD_DBNAME')
        postgres_user = os.environ.get('LIVE_PROD_USER')
        postgres_password = os.environ.get('LIVE_PROD_PASSWORD')
        postgres_sslmode = os.environ.get('LIVE_PROD_SSLMODE')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
            postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        self.local_con = psycopg2.connect(postgres_con_string)
        self.local_cur = self.local_con.cursor()
        self.local_con.autocommit = True

        # postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(postgres_user, postgres_password, postgres_host, postgres_dbname)
        # self.local_engine = sqlalchemy.create_engine(postgres_engine_string)

        self.global_logger.info("connected to prod live")

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
        self.successful_logger = self.setup_logger(
            'successful_logger', './logs/successful.log')
        self.failed_unicity_constraint_logger = self.setup_logger(
            'failed_unicity_constraint_logger', './logs/failed_unicity_constraint.log')
        self.general_error_logger = self.setup_logger(
            'general_error_logger', './logs/general_error.log')
        self.global_logger = self.setup_logger(
            'global_logger', './logs/global.log')

    def update_failed_rows(self, table_name, failing_sid, rawuid):
        insert_query = "INSERT INTO not_pushed_to_prod (table_name, failing_sid, rawuid) VALUES ({values}) ON CONFLICT DO NOTHING"
        insert_query = sql.SQL(insert_query).format(
            values=sql.SQL(', ').join(sql.Placeholder() * 3)
        )

        update_pushed_to_prod_query = "UPDATE {table} SET pushed_to_prod = -999 WHERE sid = {sid}"
        update_pushed_to_prod_query = sql.SQL(update_pushed_to_prod_query).format(
            table=sql.Identifier(table_name),
            sid=sql.Placeholder()
        )

        try:
            self.shadow_cur.execute(
                insert_query, [table_name, failing_sid, rawuid])

            self.shadow_cur.execute(
                update_pushed_to_prod_query, [failing_sid])

            self.shadow_con.commit()
        except Exception:
            pass

    def try_queries(self, shadow_query, prod_query, prod_values, sid, raw_uid, prod_table_name, table_name):
        try:
            self.local_cur.execute(prod_query, prod_values)
            if self.local_cur.rowcount == 0:
                self.update_failed_rows(table_name, sid, raw_uid)
                self.encountered_no_rows_error += 1
                return
            self.local_con.commit()
            self.shadow_cur.execute(shadow_query, [sid])
            self.shadow_con.commit()
            self.successful_logger.info("\n" + prod_query.as_string(self.local_con) + "\n" + str(
                prod_values) + "\n" + table_name + "\nsid: " + str(sid) + " raw_uid: " + str(raw_uid) + "\n")
        except psycopg2.errors.UniqueViolation:
            self.failed_unicity_constraint_logger.error("\n" + prod_query.as_string(self.local_con) + "\n" + str(
                prod_values) + "\n" + table_name + "\nsid: " + str(sid) + " raw_uid: " + str(raw_uid) + "\n")
            self.shadow_cur.execute(shadow_query, [sid])
            self.update_failed_rows(table_name, sid, raw_uid)
            self.shadow_con.commit()
            self.encountered_unicity_error += 1
        except Exception:
            self.general_error_logger.error("\n" + prod_query.as_string(self.local_con) + "\n" + str(
                prod_values) + "\n" + table_name + "\nsid: " + str(sid) + " raw_uid: " + str(raw_uid) + "\n")
            self.general_error_logger.error(
                str(traceback.print_exc(file=sys.stdout)) + "\n")
            self.encountered_general_error += 1

    def insert_row(self, values_from_table, all_rows, prod_table_name, table_name):
        rows_list = []
        for value in all_rows:
            rows_list.append(sql.Identifier(value))

        unpushed_rows = pd.DataFrame(pd.read_sql(
            "SELECT * FROM {} WHERE pushed_to_prod = 0".format(table_name), self.shadow_engine))

        for index, row_entry in unpushed_rows.iterrows():
            raw_uid = row_entry.get("rawuid")
            values_list = []
            for value in all_rows:
                data = row_entry.get(value)
                if pd.isna(data):
                    data = None
                values_list.append(data)

            insert_query = "INSERT INTO {table} ({fields}) VALUES ({values})"
            insert_query = sql.SQL(insert_query).format(
                table=sql.Identifier(prod_table_name),
                fields=sql.SQL(',').join(rows_list),
                values=sql.SQL(', ').join(sql.Placeholder() * len(values_list))
            )

            update_sql_string = "UPDATE {table} SET pushed_to_prod = 1 WHERE sid = {sid}"
            update_local_query = sql.SQL(update_sql_string).format(
                table=sql.Identifier(table_name),
                sid=sql.Placeholder()
            )

            self.try_queries(update_local_query, insert_query, values_list, row_entry.get(
                "sid"), raw_uid, prod_table_name, table_name)

    def generate_update_prod_sql(self, values_dict, unique_dict, prod_table_name, conditions_dict, update_not_nulls):
        identifiers_list = []
        # creates list of sql statements (var1 = %{} AND var2 = ${} ...etc)
        for i, (k, v) in enumerate(unique_dict.items()):
            if i == len(unique_dict)-1:
                identifiers_list.append(sql.Composed(
                    [sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]))
            else:
                identifiers_list.append(sql.Composed(
                    [sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k), sql.SQL(" AND ")]))

        null_vals_list = []
        # creates list of sql statements (var1 IS NULL AND var2 IS NULL ...etc)
        for i, (k, v) in enumerate(values_dict.items()):
            if i == len(values_dict)-1:
                null_vals_list.append(sql.Composed(
                    [sql.Identifier(k), sql.SQL(" IS NULL ")]))
            else:
                null_vals_list.append(sql.Composed(
                    [sql.Identifier(k), sql.SQL(" IS NULL "), sql.SQL("AND ")]))

        condition_vals_list = []
        if conditions_dict:
            for i, (k, v) in enumerate(conditions_dict.items()):
                # print(v)
                condition_vals_list.append(sql.Composed(
                    [sql.SQL(" AND "), sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]))

        update_prod_query = ""

        if update_not_nulls == True:
            update_prod_query = sql.SQL("UPDATE {table} SET {values} WHERE {identifiers} {additional_conditions}").format(
                table=sql.Identifier(prod_table_name),
                values=sql.SQL(', ').join(
                    sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]) for k in values_dict.keys()
                ),
                identifiers=sql.SQL('').join(
                    identifiers_list
                ),
                additional_conditions=sql.SQL('').join(
                    condition_vals_list
                ),
            )
        else:
            update_prod_query = sql.SQL("UPDATE {table} SET {values} WHERE {identifiers} {additional_conditions} AND {is_null_vals}").format(
                table=sql.Identifier(prod_table_name),
                values=sql.SQL(', ').join(
                    sql.Composed([sql.Identifier(k), sql.SQL(" = "), sql.Placeholder(k)]) for k in values_dict.keys()
                ),
                identifiers=sql.SQL('').join(
                    identifiers_list
                ),
                additional_conditions=sql.SQL('').join(
                    condition_vals_list
                ),
                is_null_vals=sql.SQL('').join(
                    null_vals_list
                ),
            )

        # print(update_prod_query)

        return update_prod_query

    def update_row(self, values_from_table, all_rows, prod_table_name, table_name, unique_cols, additional_conditions, update_not_nulls):
        rows_list = []
        for value in values_from_table:
            rows_list.append(sql.Identifier(value))

        unpushed_rows = pd.DataFrame(pd.read_sql(
            "SELECT * FROM {} WHERE pushed_to_prod = 0".format(table_name), self.shadow_engine))

        for index, row_entry in unpushed_rows.iterrows():
            # self.global_logger.info("\n")
            raw_uid = row_entry.get("rawuid")
            values_dict = {}
            for value in values_from_table:
                data = row_entry.get(value)
                if pd.isna(data):
                    data = None
                values_dict[value] = data

            unique_dict = {}
            for value in unique_cols:
                data = row_entry.get(value)
                unique_dict[value] = data

            # print(unique_dict)

            conditions_dict = {}
            if additional_conditions:
                for condition in additional_conditions:
                    split_condition = condition.replace(" ", "").split("=")
                    column = split_condition[0]
                    value = split_condition[1]
                    if value[0] != "'":
                        value = float(value)
                    # print(column, value)

                    conditions_dict[column] = value

            # print(conditions_dict)

            update_prod_query = self.generate_update_prod_sql(
                values_dict, unique_dict, prod_table_name, conditions_dict, update_not_nulls)

            update_sql_string = "UPDATE {table} SET pushed_to_prod = 1 WHERE sid = {sid}"
            update_local_query = sql.SQL(update_sql_string).format(
                table=sql.Identifier(table_name),
                sid=sql.Placeholder()
            )

            values_dict.update(unique_dict)
            values_dict.update(conditions_dict)
            # print(unique_dict)
            # print("\n\n hi", values_dict)

            self.try_queries(update_local_query, update_prod_query, values_dict, row_entry.get(
                "sid"), raw_uid, prod_table_name, table_name)

    def push_to_prod(self):
        for table_name, info in self.shadow_table_info.items():
            prod_table_name = table_name.split("__")[0]

            values_from_table = info.get("values_from_table")
            all_rows = info.get("all_rows")
            unique_cols = info.get("unique_cols")
            mode = info.get("mode")
            additional_conditions = info.get("additional_conditions")
            update_not_nulls = info.get("update_not_nulls")

            if mode == "insert":
                self.insert_row(values_from_table, all_rows,
                                prod_table_name, table_name)

            elif mode == "update":
                self.update_row(values_from_table, all_rows,
                                prod_table_name, table_name, unique_cols, additional_conditions, update_not_nulls)

        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        self.global_logger.info("Finished pushing to prod")
        self.global_logger.info(loc_dt)

        self.encountered_unicity_error = 0
        self.encountered_no_rows_error = 0
        self.encountered_not_pushed_error = 0
        self.encountered_general_error = 0

        # self.global_logger.info("Encountered {} unicity errors, {} no rows updated errors, {} not pushed errors, {} general errors".format())

        if self.encountered_unicity_error > 0 or self.encountered_no_rows_error > 0 or self.encountered_not_pushed_error > 0 or self.encountered_general_error:
            self.global_logger.info("Encountered {} unicity errors,\n {} no rows updated errors,\n {} not pushed errors,\n {} general errors\n"
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
#     self.global_logger.info("an error ocurred \n")
#     self.global_logger.info(traceback.print_exc(file=sys.stdout))

# pp = ProductionPusher()
# pp.push_to_prod()
# pp.close_cons()
