import json
import pandas as pd
import re
import sqlite3
import sys

import psa_gps_dicts.version_vFTrkLn3MMbs9wCLEBBh4s as psa_gps_v1
import psa_water_sensor_install.version_vuiiHRr2MJSGzFwSncyLP9 as psa_water_sensor_install_v1


# print(psa_gps_v1.data)

# Create a SQL connection to our SQLite database
con = sqlite3.connect("python.db")

cur = con.cursor()

data = pd.read_excel('version_vuiiHRr2MJSGzFwSncyLP9.xlsx') 

asset_names = {
    "psa gps": {
        "vFTrkLn3MMbs9wCLEBBh4s": psa_gps_v1.data
    },
    "psa water sensor install": {
        "vuiiHRr2MJSGzFwSncyLP9": psa_water_sensor_install_v1.data
    }
}

def convert_data(data, conversions):
    if not data or not conversions:
        return data

    if "to_uppercase" in conversions:
        data = data.upper()

    if "to_lowercase" in conversions:
        data = data.lower()

    if "strip_whitespace" in conversions:
        data = "".join(data.split())

    return data

def test_data(data, tests):
    if not tests:
        return True
    
    def not_null(data):
        if data:
            return True
        else:
            return False

    def check_regex(data, regex):
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

def add_cols(new_row, extra_cols):
    if not extra_cols:
        return
    for extra_col in extra_cols:
        new_row[extra_col.get("name")] = extra_col.get("value")


def split_data(names, data, seperator, indices, new_row):
    if not data:
        return new_row
    
    split = data.split(seperator)
    
    for index, name in enumerate(names):
        new_row[name] = split[indices[index]]
    
    return new_row

def convert_to_sql(data, table):
    # valid_rows.to_sql("valid_gps", con, if_exists="replace")
    # invalid_rows.to_sql("invalid_gps", con, if_exists="replace")
    
    data.to_sql(table, con, if_exists="replace")

def query_table(query):
    cur.execute(query)
    
    # for row in cur.execute('SELECT * FROM valid_gps;'):
    #     print(row)
    #     print('\n')
    # for row in cur.execute('SELECT * FROM invalid_gps;'):
    #     print(row)
    #     print('\n')

def convert_to_excel(data, file_path):
    # valid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\valid-gps.xlsx', index = False, header=True)
    # invalid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\invalid-gps.xlsx', index = False, header=True)
    data.to_excel (file_path, index = False, header=True)

def parse_forms():
    valid_rows = pd.DataFrame()
    invalid_rows = pd.DataFrame()

    def parse_form(row_entry, form_version_key):
        nonlocal temp_valid_rows
        nonlocal temp_invalid_rows
        for kobo_row in form_version_key:
            new_row = {}

            row_is_valid = True

            if kobo_row.get("extra_cols"):
                add_cols(new_row, kobo_row.get("extra_cols"))

            for data in kobo_row.get("cols_from_form"):
                converted_data = convert_data(entry.get(data.get("kobo_name")), data.get("conversions"))

                if data.get("tests"):
                    status, message = test_data(converted_data, data.get("tests"))

                if status:
                    if len(data.get("db_names")) == 1:
                        new_row[data.get("db_names")[0]] = converted_data
                    else:
                        data = split_data(data.get("db_names"), converted_data, data.get("separator"), data.get("indices"), new_row)
                else:
                    row_is_valid = False

                    if "uid" in temp_invalid_rows:
                        if not (temp_invalid_rows["uid"] == row_entry["uid"]).any():
                            # row_entry.insert({"error": message}, True)
                            print(row_entry)
                            temp_invalid_rows = temp_invalid_rows.append(row_entry, ignore_index=True)
                    else:
                        row_entry["error"] = str(data.get("db_names")) + "failed tests"
                        temp_invalid_rows = temp_invalid_rows.append(row_entry, ignore_index=True)
                    
                    break
            if row_is_valid:
                temp_valid_rows = temp_valid_rows.append(new_row, ignore_index=True)
            else:
                return False

        return True

    for index, row_entry in data.iterrows():
        temp_valid_rows = pd.DataFrame()
        temp_invalid_rows = pd.DataFrame()

        asset_name = row_entry.get("asset_name")
        entry = json.loads(row_entry.get("data"))
        form_version = entry.get("__version__")
        form_version_key = asset_names.get(asset_name).get(form_version)

        valid_row = parse_form(row_entry, form_version_key)

        if valid_row:
            valid_rows = valid_rows.append(temp_valid_rows)
        else:
            invalid_rows = invalid_rows.append(temp_invalid_rows)


    valid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\valid-gps.xlsx', index = False, header=True)
    invalid_rows.to_excel (r'C:\Users\mikah\OneDrive - North Carolina State University\docs\school\492\test\parse\invalid-gps.xlsx', index = False, header=True)

parse_forms()

con.close()