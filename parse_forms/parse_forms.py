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
import logging

# sys.path.append(r"C:\Users\mikah\Documents\etl-forms\parse_forms")

# from .assets import xform_id_string_dataframes
# from .assets import xform_id_strings
# from .assets import asset_dataframes
# from .assets import asset_names
from .assets import xform_id_strings
from .assets import xform_id_string_dataframes
# import assets.xfr
from .api_calls import get_active_farm_codes

class FormParser:
    def __init__(self, mode=None):
        load_dotenv()
        self.connect_to_mysql()
        self.create_loggers()

        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        self.global_logger.info("Starting parsing")
        self.global_logger.info(loc_dt)

        self.mode = mode

        if self.mode == "live":
            self.global_logger.info("live")
            self.connect_to_shadow_live()
        elif self.mode == "local":
            self.global_logger.info("local")
            self.connect_to_shadow_local()

        self.temp_valid_rows = pd.DataFrame()

        self.xform_id_strings = xform_id_strings.xform_id_strings
        self.xform_id_string_dataframes = xform_id_string_dataframes.xform_id_string_dataframes
        
        self.invalid_row_table_pairs = pd.DataFrame()
        self.valid_row_table_pairs = pd.DataFrame()

        self.active_farm_codes = get_active_farm_codes.create_years_object()

        self.valid_parsed_form_tables = {}
        self.invalid_parsed_form_tables = {}

        # self.encountered_unicity_error = 0
        # self.encountered__error = 0
        self.encountered_parsing_error = 0
        # self.encountered_no_rows_error = 0

    def connect_to_shadow_live(self):
        postgres_host = os.environ.get('LIVE_SHADOW_HOST')
        postgres_dbname = os.environ.get('LIVE_SHADOW_DBNAME')
        postgres_user = os.environ.get('LIVE_SHADOW_USER')
        postgres_password = os.environ.get('LIVE_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('LIVE_SHADOW_SSLMODE')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        self.postgres_con = psycopg2.connect(postgres_con_string)
        self.postgres_cur = self.postgres_con.cursor()

        postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.postgres_engine = sqlalchemy.create_engine(postgres_engine_string)

        self.global_logger.info("Connected to shadow live")
    
    def connect_to_shadow_local(self):
        postgres_host = os.environ.get('LOCAL_SHADOW_HOST')
        postgres_dbname = os.environ.get('LOCAL_SHADOW_DBNAME')
        postgres_user = os.environ.get('LOCAL_SHADOW_USER')
        postgres_password = os.environ.get('LOCAL_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('LOCAL_SHADOW_SSLMODE')
        postgres_port = os.environ.get('LOCAL_SHADOW_PORT')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        self.postgres_con = psycopg2.connect(postgres_con_string)
        self.postgres_cur = self.postgres_con.cursor()

        postgres_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        self.postgres_engine = sqlalchemy.create_engine(postgres_engine_string)

        self.global_logger.info("Connected to shadow local")

    def connect_to_mysql(self):
        mysql_host = os.environ.get('MYSQL_HOST')
        mysql_dbname = os.environ.get('MYSQL_DBNAME')
        mysql_user = os.environ.get('MYSQL_USER')
        mysql_password = os.environ.get('MYSQL_PASSWORD')
        
        # Make mysql connections
        mysql_engine_string = "mysql://{0}:{1}@{2}/{3}".format(mysql_user, mysql_password, mysql_host, mysql_dbname)
        self.mysql_engine = sqlalchemy.create_engine(mysql_engine_string)

    def setup_logger(self, name, log_file, level=logging.INFO):
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler = logging.FileHandler(log_file)        
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
    
    def create_loggers(self):
        self.successful_parse_logger = self.setup_logger('successful_parse_logger', './logs/successful_parse.log')
        self.unsuccessful_parse_logger = self.setup_logger('unsuccessful_parse_logger', './logs/unsuccessful_parse.log')
        self.global_logger = self.setup_logger('global_logger', './logs/global.log')

    def convert_data(self, data, conversions):
        if not data or not conversions:
            return data

        if "to_uppercase" in conversions:
            data = data.upper()

        if "to_lowercase" in conversions:
            data = data.lower()

        if "strip_whitespace" in conversions:
            data = "".join(data.split())

        return data

    def test_data(self, data, tests):
        if not tests:
            return True
        
        def not_null(data):
            if data:
                return True
            else:
                return False

        def check_regex(data, regex):
            if not data:
                return True
            try:
                regex = re.compile(regex)
            except Exception:
                self.global_logger.info("invalid regex")
                self.encountered_parsing_error += 1
                return False

            if re.search(regex, data):
                return True
            else:
                return False

        functions = {
            "not_null": not_null,
            "check_regex": check_regex
        }

        for test in tests:
            name_and_params = test.split(" ")
            
            if len(name_and_params) == 1:
                response = functions.get(name_and_params[0])(data)
            elif len(name_and_params) == 2:
                response = functions.get(name_and_params[0])(data, name_and_params[1])

            if response == False:
                return False, "{} failed test {}".format(data, test)

        return True, "Passed all tests"

    def add_cols(self, new_row, extra_cols):
        if not extra_cols:
            return
        for extra_col in extra_cols:
            new_row[extra_col.get("name")] = extra_col.get("value")


    def split_data(self, names, data, seperator, indices, new_row):
        if not data:
            return new_row
        
        split = data.split(seperator)
        
        for index, name in enumerate(names):
            new_row[name] = split[indices[index]]
        
        return new_row

    def convert_to_excel(self, data, file_path):
        data.to_excel (file_path, index = False, header=True)

    def close_con(self):
        self.postgres_con.close()
        self.global_logger.info("Closing connections")

    def save_all_to_excel(self):
        for key, value in self.xform_id_string_dataframes.items():
            for key_2, value_2 in value.items():
                # self.global_logger.info(value_2)
                self.convert_to_excel(value_2, r'C:\Users\mikah\Documents\etl-forms\excel_dump\{}.xlsx'.format(key_2))

        self.convert_to_excel(self.invalid_row_table_pairs, r'C:\Users\mikah\Documents\etl-forms\excel_dump\invalid_row_table_pairs.xlsx')

    def convert_to_sql(self, dataframe, table_name):
        dataframe.to_sql(table_name, self.postgres_engine, if_exists="append", index=False)

    def delete_from_table(self, table_name, uid):
        self.global_logger.info(table_name, uid)
        delete_query = "DELETE FROM {table_name} WHERE rawuid = {uid}"
        delete_query = sql.SQL(delete_query).format(
            table_name = sql.Identifier(table_name),
            uid = sql.Placeholder()
        )

        try:
            self.postgres_cur.execute(delete_query, [uid])
            self.postgres_con.commit()
        except Exception:
            self.global_logger.info("error")
            self.global_logger.info(traceback.print_exc(file=sys.stdout))
            self.encountered_parsing_error += 1

    def save_to_postgres(self):
        for key, value in self.xform_id_string_dataframes.items():
            for key_2, value_2 in value.items():
                self.convert_to_sql(value_2, key_2)

        self.convert_to_sql(self.invalid_row_table_pairs, "invalid_row_table_pairs")

    def get_valid_parsed_forms(self):
        for key, value in self.xform_id_string_dataframes.items():
            for key_2, value_2 in value.items():
                query = "SELECT DISTINCT rawuid FROM {} ORDER BY rawuid".format(key_2)

                self.postgres_cur.execute(query)
                if key_2 not in self.valid_parsed_form_tables:
                        self.valid_parsed_form_tables[key_2] = {}
                for uid in self.postgres_cur.fetchall():
                    if uid[0] not in self.valid_parsed_form_tables[key_2]:
                        self.valid_parsed_form_tables[key_2][uid[0]] = True

        # self.global_logger.info(self.valid_parsed_form_tables)
        print(self.valid_parsed_form_tables)

    def get_invalid_parsed_forms(self):
        query = "SELECT * FROM invalid_row_table_pairs ORDER BY uid"

        self.postgres_cur.execute(query)
        
        for row in self.postgres_cur.fetchall():
            # self.global_logger.info(row)
            table_name = row[5]
            uid = row[8]

            if table_name not in self.invalid_parsed_form_tables:
                self.invalid_parsed_form_tables[table_name] = {}

            if uid not in self.invalid_parsed_form_tables[table_name]:
                self.invalid_parsed_form_tables[table_name][int(uid)] = True

        # self.global_logger.info(self.invalid_parsed_form_tables)
        print(self.invalid_parsed_form_tables)

    def get_all_responses(self):
        self.data = pd.read_sql("SELECT * FROM kobo ORDER BY uid", self.mysql_engine)
    
    def cast_data(self, data, datatype):
        if not data:
            return data

        def convert_string(data):
            return str(data)

        def convert_int(data):
            return int(data)

        def convert_date(data):
            try:
                # return time.mktime(datetime.datetime.strptime(data, "%Y-%m-%d").timetuple())
                return datetime.datetime.strptime(data, "%Y-%m-%d")
            except Exception:
                self.global_logger.info("not a valid date")
                self.encountered_parsing_error += 1
                return data
        
        data_types = {
            "string": convert_string,
            "int": convert_int,
            "date": convert_date
        }

        return data_types.get(datatype)(data)

    def test_and_format_data(self, data, entry, new_row):
        converted_data = self.convert_data(entry.get(data.get("kobo_name")), data.get("conversions"))

        status = True

        if data.get("tests"):
            status, message = self.test_data(converted_data, data.get("tests"))

        if data.get("datatype"):
            converted_data = self.cast_data(converted_data, data.get("datatype"))

        if data.get("multi_select"):
            converted_data = data.get("multi_select").get(converted_data)

        return status, converted_data

    def validate_row(self, kobo_row, new_row):
        row_is_complete_or_null = False
        
        existing_rows = 0
        for col in kobo_row.get("completeness_cols"):
            if new_row.get(col):
                existing_rows += 1

        if existing_rows == 0 or existing_rows == len(kobo_row.get("completeness_cols")):
            row_is_complete_or_null = True

        if row_is_complete_or_null:
            return True
        
        else:
            return False

    def row_is_not_null(self, kobo_row, new_row):
        if not kobo_row.get("all_cols"):
            return True
            
        row_is_not_null = False

        for col in kobo_row.get("all_cols"):
            if new_row.get(col):
                row_is_not_null = True
                break

        if row_is_not_null:
            return True
        
        else:
            return False

    def assert_active(self, new_row, entry):
        message = "Valid farm code"

        farm_code = new_row.get("code")
        end = entry.get("end")
        year = ""
        month = ""
        if end:
            date = end.split("-")
            year = date[0]
            month = date[1]
        
        if not farm_code:
            return True, message

        active_farms_for_year = self.active_farm_codes.get(year)
        if int(month) >= 10:
            active_farms_for_year.update(self.active_farm_codes.get(str(int(year) + 1)))
        elif int(month) <= 3:
            active_farms_for_year.update(self.active_farm_codes.get(str(int(year) - 1)))

        if active_farms_for_year:
            if active_farms_for_year.get(farm_code):
                return True, message
            else:
                message = "No farm code " + str(farm_code) + " for " + str(year)
                return False, message
        else:
            message = "No data " + " for " + str(year)
            return False, message

    def get_cols_from_form(self, kobo_row, entry, new_row, table_name):
        row_passed_tests = True
        error_message = ""

        for data in kobo_row.get("cols_from_form"):
            status, converted_data = self.test_and_format_data(data, entry, new_row)

            if status:
                if not data.get("separator"):
                    new_row[data.get("db_names")[0]] = converted_data
                else:
                    data = self.split_data(data.get("db_names"), converted_data, data.get("separator"), data.get("indices"), new_row)
            else:
                row_passed_tests = False
                error_message = str(data.get("kobo_name")) + " row failed tests for table " + table_name
                break

        return row_passed_tests, error_message


    def parse_form(self, row_entry, form_version_key, table_name):
        entry = json.loads(row_entry.get("data"))
        
        empty_form = True
        for kobo_row in form_version_key:
            new_row = {
                "rawuid": row_entry.get("uid"),
                "parsed_at": datetime.datetime.now()
            }
            
            if kobo_row.get("extra_cols"):
                self.add_cols(new_row, kobo_row.get("extra_cols"))

            row_passed_tests, error_message = self.get_cols_from_form(kobo_row, entry, new_row, table_name)
            
            row_is_valid = True
            if kobo_row.get("completeness_cols") and row_passed_tests:
                row_is_valid = self.validate_row(kobo_row, new_row)
                
                if not row_is_valid:
                    error_message = str(kobo_row.get("completeness_cols")) + " failed completeness cols for table " + table_name #+ " row data = " + json.dumps(new_row)

            active_farm, farm_message = self.assert_active(new_row, entry)

            if not active_farm:
                error_message = farm_message

            if (not row_passed_tests or not row_is_valid or not active_farm):
                return False, error_message

            elif self.row_is_not_null(kobo_row, new_row):
                new_row["pushed_to_prod"] = 0
                self.temp_valid_rows = self.temp_valid_rows.append(new_row, ignore_index=True)
                empty_form = False

        if empty_form:
            return False, "empty form"
        else:
            return True, "success"

    def iterate_tables(self, table_list, asset_name, row_entry, form_version, xform_id_string, not_reparse = True):
        for table in table_list:
            self.temp_valid_rows = pd.DataFrame()
            valid_row_table_pairs = None
            table_name = None
            table_name = table.get("table_name")
            row_uid = row_entry.get("uid")

            # print("start " + str(row_uid))


            if not_reparse and self.valid_parsed_form_tables and self.valid_parsed_form_tables.get(table_name).get(row_uid):
                # print("valid row " + str(row_uid))
                continue
            if not_reparse and self.invalid_parsed_form_tables and self.invalid_parsed_form_tables.get(table_name).get(row_uid):
                # print("invalid row " + str(row_uid))
                continue
            
            if table_name in self.xform_id_string_dataframes.get(xform_id_string):
                valid_row_table_pairs = self.xform_id_string_dataframes.get(xform_id_string).get(table_name)
            else:
                continue

            table_key = table.get("table_keys").get(form_version)

            

            if table_key:
                valid_row, message = self.parse_form(row_entry, table_key, table.get("table_name"))

                if valid_row:
                    self.successful_parse_logger.info("successfully parsed form uid {} for table {}".format(row_uid, table_name))
                    self.xform_id_string_dataframes.get(xform_id_string)[table_name] = valid_row_table_pairs.append(self.temp_valid_rows, ignore_index=True)
                else:
                    row_entry["table_name"] = table_name
                    row_entry["err"] = message
                    row_entry["xform_id_string"] = xform_id_string
                    self.invalid_row_table_pairs = self.invalid_row_table_pairs.append(row_entry, ignore_index=True)
                    row_entry.pop("err")
                    self.unsuccessful_parse_logger.error("could not parse form uid {} for table {}".format(row_uid, table_name))
                    self.encountered_parsing_error += 1

    def update_table(self, dataframe, table_name, uid):
        self.delete_from_table(table_name, uid)
        self.convert_to_sql(dataframe, table_name)

    def update_reparsed_rows(self, xform_id_string, uid):
        print(self.invalid_row_table_pairs)

        for key, value in self.xform_id_string_dataframes.get(xform_id_string).items():
            # print(value)
            self.update_table(value, key, uid)
    
    def reparse_form(self, uid):
        row_entry = pd.read_sql("SELECT * FROM kobo WHERE uid = {}".format(uid), self.mysql_engine).iloc[0]
        # self.global_logger.info(type(row_entry))
        # self.global_logger.info(row_entry.get("data"))
        asset_name = row_entry.get("asset_name")
        entry = json.loads(row_entry.get("data"))
        form_version = entry.get("__version__")

        table_list = self.xform_id_strings.get(asset_name)

        if table_list:
            self.iterate_tables(table_list, asset_name, row_entry, form_version, False)

        self.update_reparsed_rows(asset_name, uid)
        

    def parse_forms(self):
        self.get_valid_parsed_forms()
        self.get_invalid_parsed_forms()
        self.get_all_responses()

        for index, row_entry in self.data.iterrows():
            # print("start " + str(row_entry.get("uid")))
            asset_name = row_entry.get("asset_name")
            entry = json.loads(row_entry.get("data"))
            form_version = entry.get("__version__")
            xform_id_string = entry.get("_xform_id_string")

            table_list = self.xform_id_strings.get(xform_id_string)
            # print(table_list)

            if table_list:
                self.iterate_tables(table_list, asset_name, row_entry, form_version, xform_id_string)
            else:
                print("no table list " + str(row_entry.get("uid")))

        
        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        self.global_logger.info("Saving to sql")
        self.global_logger.info(loc_dt)

        if self.encountered_parsing_error > 0:
            self.global_logger.info("Encountered {} parsing errors".format(self.encountered_parsing_error))

        self.save_to_postgres()


# try:
#     mode = None
#     uid = None
#     if len(sys.argv) > 1:
#         mode = sys.argv[1]  
#         if len(sys.argv) > 2:
#             uid = sys.argv[2]

#     fp = FormParser(mode)
#     if mode == "test" or mode == "live" or mode == None:
#         fp.parse_forms()
#     elif mode == "reparse":
#         fp.reparse_form(uid)

#     fp.close_con()

# except Exception:
#     self.global_logger.info("an error ocurred \n")
#     self.global_logger.info(traceback.print_exc(file=sys.stdout))