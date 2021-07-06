import json
import pandas as pd
import re
import sqlite3
import sys
import time
import datetime

import assets.asset_dataframes
import assets.asset_names
import api_calls.get_active_farm_codes

class FormParser:
    con = sqlite3.connect('sqlite_dbs/shadow_tables.db')
    cur = con.cursor()

    data = pd.read_csv('all_data.csv') 

    temp_valid_rows = pd.DataFrame()

    asset_names = assets.asset_names.asset_names
    asset_dataframes = assets.asset_dataframes.asset_dataframes
    invalid_rows = pd.DataFrame()
    valid_rows = pd.DataFrame()

    # active_farm_codes = api_calls.get_active_farm_codes.create_years_object()

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
                print("invalid regex")
                return False

            if re.search(regex, data):
                return True
            else:
                return False

        functions = {
            "not_null": not_null,
            "check_reqex": check_regex
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
        # valid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\valid-gps.xlsx', index = False, header=True)
        # invalid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\invalid-gps.xlsx', index = False, header=True)
        data.to_excel (file_path, index = False, header=True)

    # def test_data(self, data):

    def close_con(self):
        self.con.close()

    def save_all_to_excel(self):
        for key, value in self.asset_dataframes.items():
            for key_2, value_2 in value.items():
                # print(value_2)
                self.convert_to_excel(value_2, r'C:\Users\mikah\Documents\etl-forms\excel_dump\{}.xlsx'.format(key_2))

        self.convert_to_excel(self.invalid_rows, r'C:\Users\mikah\Documents\etl-forms\excel_dump\invalid_rows.xlsx')
        self.convert_to_excel(self.valid_rows, r'C:\Users\mikah\Documents\etl-forms\excel_dump\valid_rows.xlsx')

    def query_table(self, table_name, query):
        con = sqlite3.connect('sqlite_dbs/{}.db'.format(table_name))
        cur = con.cursor()
        cur.execute(query)
        
        # for row in cur.execute('SELECT * FROM valid_gps;'):
        #     print(row)
        #     print('\n')
        # for row in cur.execute('SELECT * FROM invalid_gps;'):
        #     print(row)
        #     print('\n')

    def insert_new_rows(self, dataframe, table_name):
        # print(table_name + "\n")
        # print(dataframe)
        dataframe.to_sql("temp_table", self.con, if_exists="replace")

        # query = """\
        #     DELETE FROM {}
        # """.format(table_name)

        query = """\
            INSERT INTO {}
            SELECT *
            FROM temp_table
            WHERE rawuid NOT IN
                (SELECT rawuid 
                FROM {})
        """.format(table_name, table_name)

        print(query)

        self.cur.execute(query)
        self.con.commit()

    def convert_to_sql(self, dataframe, table_name):
        # valid_rows.to_sql("valid_gps", con, if_exists="replace")
        # invalid_rows.to_sql("invalid_gps", con, if_exists="replace")
        
        dataframe.to_sql(table_name, self.con, if_exists="append")

    # def save_to_sqlite(self, dataframe, table_name):
    #     # con = sqlite3.connect('sqlite_dbs/{}.db'.format(db_name))
    #     # cur = con.cursor()
    #     self.convert_to_sql(dataframe, table_name)

    def save_all_to_sqlite(self):
        for key, value in self.asset_dataframes.items():
            for key_2, value_2 in value.items():
                # print(value_2)
                self.insert_new_rows(value_2, key_2)

        # self.convert_to_sql(self.invalid_rows, "invalid_rows")
        # self.convert_to_sql(self.valid_rows, "valid_rows")
    
    def cast_data(self, data, datatype):
        if not data:
            return data

        def convert_string(data):
            return str(data)

        def convert_int(data):
            return int(data)

        def convert_date(data):
            return time.mktime(datetime.datetime.strptime(data, "%Y-%m-%d").timetuple())
        
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
        return True, message

        farm_code = new_row.get("code")
        end = entry.get("end")
        year = ""
        if end:
            year = end.split("-")[0]
        
        if not farm_code:
            return True, message

        active_farms_for_year = self.active_farm_codes.get(year)

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
        
        for kobo_row in form_version_key:
            new_row = {
                "rawuid": row_entry.get("uid"),
                "parsed_at": time.time()
            }
            
            if kobo_row.get("extra_cols"):
                self.add_cols(new_row, kobo_row.get("extra_cols"))

            row_passed_tests, error_message = self.get_cols_from_form(kobo_row, entry, new_row, table_name)
            
            row_is_valid = True
            if kobo_row.get("completeness_cols") and row_passed_tests:
                row_is_valid = self.validate_row(kobo_row, new_row)
                
                if not row_is_valid:
                    error_message = str(kobo_row.get("completeness_cols")) + " failed completeness cols for table " + table_name + " row data = " + json.dumps(new_row)

            active_farm, farm_message = self.assert_active(new_row, entry)

            if not active_farm:
                error_message = farm_message

            if (not row_passed_tests or not row_is_valid or not active_farm):
                return False, error_message

            elif self.row_is_not_null(kobo_row, new_row):
                    new_row["pushed_to_prod"] = 0
                    self.temp_valid_rows = self.temp_valid_rows.append(new_row, ignore_index=True)

        return True, "success"

    def iterate_tables(self, table_list, asset_name, row_entry, form_version):
        error_message = ""
        all_rows_are_valid = True
        for table in table_list:
            self.temp_valid_rows = pd.DataFrame()
            valid_rows = None
            table_name = None

            table_name = table.get("table_name")
            if table_name in self.asset_dataframes.get(asset_name):
                valid_rows = self.asset_dataframes.get(asset_name).get(table_name)
            else:
                row_entry["error"] = "no dataframes added"
                row_entry["table_name"] = table_name
                self.invalid_rows = self.invalid_rows.append(row_entry, ignore_index=True)
                continue

            table_key = table.get("table_keys").get(form_version)

            if table_key:
                valid_row, message = self.parse_form(row_entry, table_key, table.get("table_name"))

                if valid_row:
                    self.asset_dataframes.get(asset_name)[table_name] = valid_rows.append(self.temp_valid_rows, ignore_index=True)
                    row_entry["table_name"] = table_name
                    self.valid_rows = self.valid_rows.append(row_entry, ignore_index=True)
                else:
                    row_entry["table_name"] = table_name
                    row_entry["error"] = message
                    self.invalid_rows = self.invalid_rows.append(row_entry, ignore_index=True)
                    all_rows_are_valid = False
                    row_entry.pop("error")
            else:
                row_entry["table_name"] = table_name
                row_entry["error"] = "no key available"
                self.invalid_rows = self.invalid_rows.append(row_entry, ignore_index=True)
                all_rows_are_valid = False
                row_entry.pop("error")

        if all_rows_are_valid:
            return True, "all rows are valid"
        else:
            return False, error_message

    def parse_forms(self):
        for index, row_entry in self.data.iterrows():
            asset_name = row_entry.get("asset_name")
            entry = json.loads(row_entry.get("data"))
            form_version = entry.get("__version__")

            table_list = self.asset_names.get(asset_name)

            if table_list:
                self.iterate_tables(table_list, asset_name, row_entry, form_version)
            else:
                error_message = "no table list"
                row_entry["error"] = error_message
                self.invalid_rows = self.invalid_rows.append(row_entry, ignore_index=True)

        self.save_all_to_excel()
        self.save_all_to_sqlite()
    
fp = FormParser()
fp.parse_forms()
fp.close_con()