import json
import pandas as pd
import re
import sys
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

from .assets import xform_id_strings
from .assets import xform_id_string_dataframes
from .api_calls import get_active_farm_codes
from .api_calls import get_producers


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
        self.valid_producers = get_producers.create_producers_object()

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
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
            postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        self.postgres_con = psycopg2.connect(postgres_con_string)
        self.postgres_cur = self.postgres_con.cursor()

        postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(
            postgres_user, postgres_password, postgres_host, postgres_dbname)
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
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(
            postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        self.postgres_con = psycopg2.connect(postgres_con_string)
        self.postgres_cur = self.postgres_con.cursor()

        postgres_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
            postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        self.postgres_engine = sqlalchemy.create_engine(postgres_engine_string)

        self.global_logger.info("Connected to shadow local")

    def connect_to_mysql(self):
        mysql_host = os.environ.get('MYSQL_HOST')
        mysql_dbname = os.environ.get('MYSQL_DBNAME')
        mysql_user = os.environ.get('MYSQL_USER')
        mysql_password = os.environ.get('MYSQL_PASSWORD')

        # Make mysql connections
        mysql_engine_string = "mysql://{0}:{1}@{2}/{3}".format(
            mysql_user, mysql_password, mysql_host, mysql_dbname)
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
        self.successful_parse_logger = self.setup_logger(
            'successful_parse_logger', './logs/successful_parse.log')
        self.unsuccessful_parse_logger = self.setup_logger(
            'unsuccessful_parse_logger', './logs/unsuccessful_parse.log')
        self.global_logger = self.setup_logger(
            'global_logger', './logs/global.log')

    def convert_data(self, data, conversions):
        if not data or not conversions:
            return data

        if "to_uppercase" in conversions:
            data = data.upper()

        if "to_lowercase" in conversions:
            data = data.lower()

        if "strip_whitespace" in conversions:
            data = "".join(data.split())

        if "numbers_only" in conversions:
            numeric_filter = filter(str.isdigit, data)
            data = "".join(numeric_filter)

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
                response = functions.get(name_and_params[0])(
                    data, name_and_params[1])

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

    # def convert_to_excel(self, data, file_path):
    #     data.to_excel (file_path, index = False, header=True)

    def close_con(self):
        self.postgres_con.close()
        self.global_logger.info("Closing connections")

    # def save_all_to_excel(self):
    #     for key, value in self.xform_id_string_dataframes.items():
    #         for key_2, value_2 in value.items():
    #             # self.global_logger.info(value_2)
    #             self.convert_to_excel(value_2, r'C:\Users\mikah\Documents\etl-forms\excel_dump\{}.xlsx'.format(key_2))

    #     self.convert_to_excel(self.invalid_row_table_pairs, r'C:\Users\mikah\Documents\etl-forms\excel_dump\invalid_row_table_pairs.xlsx')

    def convert_to_sql(self, dataframe, table_name):
        dataframe.to_sql(table_name, self.postgres_engine,
                         if_exists="append", index=False)

    def save_to_postgres(self):
        for key, value in self.xform_id_string_dataframes.items():
            for key_2, value_2 in value.items():
                self.convert_to_sql(value_2, key_2)

        self.convert_to_sql(self.invalid_row_table_pairs,
                            "invalid_row_table_pairs")

    def get_valid_parsed_forms(self):
        for key, value in self.xform_id_string_dataframes.items():
            for key_2, value_2 in value.items():
                query = "SELECT DISTINCT rawuid FROM {} ORDER BY rawuid".format(
                    key_2)

                self.postgres_cur.execute(query)
                if key_2 not in self.valid_parsed_form_tables:
                    self.valid_parsed_form_tables[key_2] = {}
                for uid in self.postgres_cur.fetchall():
                    if uid[0] not in self.valid_parsed_form_tables[key_2]:
                        self.valid_parsed_form_tables[key_2][uid[0]] = True

    def get_invalid_parsed_forms(self):
        query = "SELECT * FROM invalid_row_table_pairs ORDER BY uid"

        self.postgres_cur.execute(query)

        for row in self.postgres_cur.fetchall():
            table_name = row[5]
            uid = row[8]

            if table_name not in self.invalid_parsed_form_tables:
                self.invalid_parsed_form_tables[table_name] = {}

            if uid not in self.invalid_parsed_form_tables[table_name]:
                self.invalid_parsed_form_tables[table_name][int(uid)] = True

    def get_all_responses(self):
        self.data = pd.read_sql(
            "SELECT * FROM kobo ORDER BY uid", self.mysql_engine)

    def cast_data(self, data, datatype):
        if not data:
            return data

        def convert_string(data):
            return str(data)

        def convert_int(data):
            return int(data)

        def convert_date(data):
            try:
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

    def test_and_format_data(self, data, row_data):
        converted_data = self.convert_data(row_data.get(
            data.get("kobo_name")), data.get("conversions"))

        status = True

        if data.get("tests"):
            status, message = self.test_data(converted_data, data.get("tests"))

        if data.get("datatype"):
            converted_data = self.cast_data(
                converted_data, data.get("datatype"))

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

    def assert_active(self, new_row, row_data, end):
        message = "Valid farm code"

        farm_code = new_row.get("code")

        if not end:
            end = row_data.get("end")

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
            active_farms_for_year.update(
                self.active_farm_codes.get(str(int(year) + 1)))
        elif int(month) <= 3:
            active_farms_for_year.update(
                self.active_farm_codes.get(str(int(year) - 1)))

        if active_farms_for_year:
            if active_farms_for_year.get(farm_code):
                return True, message
            else:
                message = "No farm code " + \
                    str(farm_code) + " for " + str(year)
                return False, message
        else:
            message = "No data " + " for " + str(year)
            return False, message

    def get_producer_id(self, new_row):
        if new_row.get("producer_phone") and self.valid_producers.get(new_row.get("producer_phone")):
            return self.valid_producers.get(new_row.get("producer_phone"))
        elif new_row.get("producer_email") and self.valid_producers.get(new_row.get("producer_email")):
            return self.valid_producers.get(new_row.get("producer_email"))
        else:
            return False

    def validate_gps_points(self, form_rows):
        # row_obj = {
        #     "C1": [],
        #     "C2": [],
        #     "B1": [],
        #     "B2": [],
        # }

        row_obj = {}

        for index, row in form_rows.iterrows():
            if not row_obj.get(row["treatment"] + str(int(row["subplot"]))):
                row_obj[row["treatment"] + str(int(row["subplot"]))] = []
            row_obj[row["treatment"] + str(int(row["subplot"]))
                    ].append((pd.isna(row.get("latitude")) or pd.isna(row.get("longitude"))))

        valid_form = True

        for key in row_obj:
            if any(row_obj.get(key)) and not(all(row_obj.get(key))):
                valid_form = False

        return valid_form

    def get_cols_from_form(self, kobo_row, row_data, new_row, table_name):
        row_passed_tests = True
        error_messages = []

        for data in kobo_row.get("cols_from_form"):
            status, converted_data = self.test_and_format_data(data, row_data)

            if status:
                if not data.get("separator"):
                    new_row[data.get("db_names")[0]] = converted_data
                else:
                    data = self.split_data(data.get("db_names"), converted_data, data.get(
                        "separator"), data.get("indices"), new_row)
            else:
                row_passed_tests = False
                error_messages.append(
                    "`[\"" + str(data.get("kobo_name")) + "\"]`" + " row failed tests for table " + table_name)
                # break

        return row_passed_tests, error_messages

    def extract_row(self, row_uid, kobo_row, row_data, table_name, error_list, empty_form, valid_producer, end=False, submitted_by=False):
        new_row = {
            "rawuid": row_uid,
            "parsed_at": datetime.datetime.now()
        }

        if kobo_row.get("extra_cols"):
            self.add_cols(new_row, kobo_row.get("extra_cols"))

        row_passed_tests, error_messages = self.get_cols_from_form(
            kobo_row, row_data, new_row, table_name)

        error_list += error_messages

        row_is_valid = True
        if kobo_row.get("completeness_cols") and row_passed_tests:
            row_is_valid = self.validate_row(kobo_row, new_row)

            if not row_is_valid:
                error_message = "`" + json.dumps(kobo_row.get("completeness_errs")) + "` " + str(
                    kobo_row.get("completeness_err_message")) + " for table " + table_name
                error_list += [error_message]

        active_farm, farm_message = self.assert_active(new_row, row_data, end)

        if kobo_row.get("verify_producer") and row_passed_tests:
            producer_id = self.get_producer_id(new_row)
            if producer_id:
                new_row["producer_id"] = producer_id
            else:
                error_list += ["producer with that email or phone does not exist"]
                valid_producer = False

        if not active_farm and farm_message not in error_list:
            error_list += [farm_message]

        if self.row_is_not_null(kobo_row, new_row):
            empty_form = False

        if submitted_by:
            new_row['submitted_by'] = submitted_by

        if row_passed_tests and row_is_valid and active_farm and self.row_is_not_null(kobo_row, new_row) and valid_producer:
            new_row["pushed_to_prod"] = 0
            self.temp_valid_rows = self.temp_valid_rows.append(
                new_row, ignore_index=True)

        return error_list, empty_form, valid_producer

    def parse_nested_form(self, row_uid, kobo_row, row_data, table_name, error_list, empty_form, valid_producer):
        entry_to_iterate = kobo_row.get("entry_to_iterate")
        end = row_data.get("end")
        submitted_by = row_data.get("_submitted_by")
        print(submitted_by)
        for item in row_data.get(entry_to_iterate):
            error_list, empty_form, valid_producer = self.extract_row(
                row_uid, kobo_row, item, table_name, error_list, empty_form, valid_producer, end, submitted_by)

        return error_list, empty_form, valid_producer

    def parse_form(self, form_version_key, table_name, row_data, row_uid):
        empty_form = True
        valid_producer = True
        error_list = []
        valid_gps_form = True

        for kobo_row in form_version_key:
            if kobo_row.get("entry_to_iterate"):
                error_list, empty_form, valid_producer = self.parse_nested_form(
                    row_uid, kobo_row, row_data, table_name, error_list, empty_form, valid_producer)
            else:
                error_list, empty_form, valid_producer = self.extract_row(
                    row_uid, kobo_row, row_data, table_name, error_list, empty_form, valid_producer)

        if table_name == "gps_corners__gps":
            valid_gps_form = self.validate_gps_points(self.temp_valid_rows)
            if valid_gps_form == False:
                print("invalid gps form")
                error_list.append("GPS points missing for one or more plots")

        if empty_form:
            error_list.append("Empty form" + " for table " + table_name)
        if len(error_list) != 0:
            return False, error_list
        else:
            return True, "success"

    def iterate_tables(self, table_list, row_entry, row_uid, row_data, form_version, xform_id_string, not_reparse=True):
        for table in table_list:
            self.temp_valid_rows = pd.DataFrame()
            valid_row_table_pairs = None
            table_name = table.get("table_name")

            table_key = table.get("table_keys").get(form_version)

            if (not_reparse and self.valid_parsed_form_tables and self.valid_parsed_form_tables.get(table_name) and self.valid_parsed_form_tables.get(table_name).get(row_uid)) \
                    or (not_reparse and self.invalid_parsed_form_tables and self.invalid_parsed_form_tables.get(table_name) and self.invalid_parsed_form_tables.get(table_name).get(row_uid)):

                continue

            if table_name in self.xform_id_string_dataframes.get(xform_id_string):
                valid_row_table_pairs = self.xform_id_string_dataframes.get(
                    xform_id_string).get(table_name)
            else:
                continue

            if table_key:
                valid_row, messages = self.parse_form(
                    table_key, table_name, row_data, row_uid)

                if valid_row:
                    self.successful_parse_logger.info(
                        "successfully parsed form uid {} for table {}".format(row_uid, table_name))
                    self.xform_id_string_dataframes.get(xform_id_string)[
                        table_name] = valid_row_table_pairs.append(self.temp_valid_rows, ignore_index=True)
                else:
                    row_entry["table_name"] = table_name
                    row_entry["err"] = json.dumps(messages)
                    row_entry["xform_id_string"] = xform_id_string
                    self.invalid_row_table_pairs = self.invalid_row_table_pairs.append(
                        row_entry, ignore_index=True)
                    row_entry.pop("err")
                    self.unsuccessful_parse_logger.error(
                        "could not parse form uid {} for table {}".format(row_uid, table_name))
                    self.encountered_parsing_error += 1

    # def update_table(self, dataframe, table_name, uid):
    #     self.delete_from_table(table_name, uid)
    #     self.convert_to_sql(dataframe, table_name)

    # def update_reparsed_rows(self, xform_id_string, uid):
    #     # print(self.invalid_row_table_pairs)

    #     for key, value in self.xform_id_string_dataframes.get(xform_id_string).items():
    #         # print(value)
    #         self.update_table(value, key, uid)

    # def reparse_form(self, uid):
    #     row_entry = pd.read_sql("SELECT * FROM kobo WHERE uid = {}".format(uid), self.mysql_engine).iloc[0]
    #     # self.global_logger.info(type(row_entry))
    #     # self.global_logger.info(row_entry.get("data"))
    #     asset_name = row_entry.get("asset_name")
    #     row_data = json.loads(row_entry.get("data"))
    #     form_version = row_data.get("__version__")

    #     table_list = self.xform_id_strings.get(asset_name)

    #     if table_list:
    #         self.iterate_tables(table_list, asset_name, row_entry, form_version, False)

    #     self.update_reparsed_rows(asset_name, uid)

    def parse_forms(self):
        self.get_valid_parsed_forms()
        self.get_invalid_parsed_forms()
        self.get_all_responses()

        for index, row_entry in self.data.iterrows():
            # print("start " + str(row_entry.get("uid")))
            row_data = json.loads(row_entry.get("data"))
            form_version = row_data.get("__version__")
            xform_id_string = row_data.get("_xform_id_string")
            row_uid = row_entry.get("uid")
            row_data = json.loads(row_entry.get("data"))

            table_list = self.xform_id_strings.get(xform_id_string)
            # print(table_list)

            if table_list:
                self.iterate_tables(
                    table_list, row_entry, row_uid, row_data, form_version, xform_id_string)
            else:
                print("no table list " + str(row_entry.get("uid")))

        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        self.global_logger.info("Saving to sql")
        self.global_logger.info(loc_dt)

        if self.encountered_parsing_error > 0:
            self.global_logger.info("Encountered {} parsing errors".format(
                self.encountered_parsing_error))

        print(
            self.xform_id_string_dataframes["aZjGUZ6htFZV5hFgxjP4oa"]["farm_history__farm_history_survey"])

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
