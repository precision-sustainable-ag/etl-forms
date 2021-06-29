import json
import pandas as pd
import re
import sqlite3
import sys
import time
import datetime

import assets.asset_dataframes
import assets.asset_names

class FormParser:
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect('sqlite_dbs/python.db')

    cur = con.cursor()

    data = pd.read_csv('all_data.csv') 

    temp_valid_rows = pd.DataFrame()
    temp_invalid_rows = pd.DataFrame()

    asset_names = assets.asset_names.asset_names
    asset_dataframes = assets.asset_dataframes.asset_dataframes
    invalid_rows = pd.DataFrame()

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

    def convert_to_sql(self, data, table):
        # valid_rows.to_sql("valid_gps", con, if_exists="replace")
        # invalid_rows.to_sql("invalid_gps", con, if_exists="replace")
        
        data.to_sql(table, con, if_exists="replace")

    def convert_to_excel(self, data, file_path):
        # valid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\valid-gps.xlsx', index = False, header=True)
        # invalid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\invalid-gps.xlsx', index = False, header=True)
        data.to_excel (file_path, index = False, header=True)

    def query_table(self, query):
        cur.execute(query)
        
        # for row in cur.execute('SELECT * FROM valid_gps;'):
        #     print(row)
        #     print('\n')
        # for row in cur.execute('SELECT * FROM invalid_gps;'):
        #     print(row)
        #     print('\n')

    # def test_data(self, data):

    def close_con(self):
        self.con.close()

    def save_all_to_excel(self, asset_dataframes):
        for key, value in asset_dataframes.items():
            for key_2, value_2 in value.items():
                print(value_2)
                self.convert_to_excel(value_2, r'C:\Users\mikah\Documents\etl-forms\excel_dump\{}.xlsx'.format(key_2))
                self.convert_to_excel(self.invalid_rows, r'C:\Users\mikah\Documents\etl-forms\excel_dump\invalid_rows.xlsx')
    
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

    def parse_form(self, row_entry, form_version_key):
        entry = json.loads(row_entry.get("data"))
        
        for kobo_row in form_version_key:
            new_row = {}

            row_passed_tests = True

            if kobo_row.get("extra_cols"):
                self.add_cols(new_row, kobo_row.get("extra_cols"))

            for data in kobo_row.get("cols_from_form"):
                status, converted_data = self.test_and_format_data(data, entry, new_row)

                if status:
                    if not data.get("separator"):
                        new_row[data.get("db_names")[0]] = converted_data
                    else:
                        data = self.split_data(data.get("db_names"), converted_data, data.get("separator"), data.get("indices"), new_row)
                else:
                    row_passed_tests = False

                    if "uid" in self.temp_invalid_rows:
                        if not (self.temp_invalid_rows["uid"] == row_entry["uid"]).any():
                            self.temp_invalid_rows = self.temp_invalid_rows.append(row_entry, ignore_index=True)
                    else:
                        row_entry["error"] = str(data.get("kobo_name")) + " failed tests"
                        self.temp_invalid_rows = self.temp_invalid_rows.append(row_entry, ignore_index=True)
                    
                    break

            if row_passed_tests:
                if kobo_row.get("completeness_cols"):

                    row_is_not_null = False
                    row_is_complete = False

                    for col in kobo_row.get("all_cols"):
                        if new_row.get(col) != None:
                            row_is_not_null = True
                            break
                    
                    existing_rows = 0
                    for col in kobo_row.get("completeness_cols"):
                        if new_row.get(col) != None:
                            existing_rows += 1

                    if existing_rows == 0 or existing_rows == len(kobo_row.get("completeness_cols")):
                        row_is_complete = True

                    if row_is_complete and row_is_not_null:
                        new_row["rawuid"] = row_entry.get("uid")
                        new_row["parsed_at"] = time.time()
                        self.temp_valid_rows = self.temp_valid_rows.append(new_row, ignore_index=True)
                    else:
                        row_entry["error"] = str(kobo_row.get("completeness_cols")) + " failed completeness cols"
                        self.temp_invalid_rows = self.temp_invalid_rows.append(row_entry, ignore_index=True)
                else:
                    self.temp_valid_rows = self.temp_valid_rows.append(new_row, ignore_index=True)
            else:
                return False

        return True

    def parse_forms(self):
        for index, row_entry in self.data.iterrows():
            self.temp_valid_rows = pd.DataFrame()
            self.temp_invalid_rows = pd.DataFrame()
            # global asset_names

            asset_name = row_entry.get("asset_name")
            entry = json.loads(row_entry.get("data"))
            form_version = entry.get("__version__")

            table_list = self.asset_names.get(asset_name)

            # if 

            if table_list:
                for table in table_list:
                    valid_rows = None
                    invalid_rows = self.invalid_rows
                    table_name = None

                    # print(self.asset_dataframes.get(asset_name))
                    table_name = table.get("table_name")
                    # print(table_name)
                    if table_name in self.asset_dataframes.get(asset_name):
                        # print("got it")
                        # print(self.asset_dataframes.get(asset_name))
                        valid_rows = self.asset_dataframes.get(asset_name).get(table_name)
                        # invalid_rows = self.asset_dataframes.get(asset_name).get(table_name)
                    else:
                        row_entry["error"] = "no dataframes added"
                        # print("no dataframes")
                        # invalid_rows = invalid_rows.append(row_entry, ignore_index=True)
                        continue

                    table_key = table.get("table_keys").get(form_version)

                    if table_key:
                        valid_row = self.parse_form(row_entry, table_key)

                        if valid_row:
                            self.asset_dataframes.get(asset_name)[table_name] = valid_rows.append(self.temp_valid_rows)
                        else:
                            self.invalid_rows = invalid_rows.append(self.temp_invalid_rows)
                    else:
                        row_entry["error"] = "no key available"
                        self.invalid_rows = invalid_rows.append(row_entry, ignore_index=True)

            else:
                row_entry["error"] = "no key available"
                self.invalid_rows = invalid_rows.append(row_entry, ignore_index=True)

        self.save_all_to_excel(self.asset_dataframes)
    
fp = FormParser()
fp.parse_forms()
fp.close_con()