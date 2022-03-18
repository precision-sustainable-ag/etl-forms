# to run use 'python -m helper_functions.get_all_versions.py' from ./etl-forms

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

import parse_forms.assets.xform_id_strings as xform_id_strings


class FormParser:
    def __init__(self):
        load_dotenv()
        self.connect_to_mysql()

    def connect_to_mysql(self):
        mysql_host = os.environ.get('MYSQL_HOST')
        mysql_dbname = os.environ.get('MYSQL_DBNAME')
        mysql_user = os.environ.get('MYSQL_USER')
        mysql_password = os.environ.get('MYSQL_PASSWORD')

        # Make mysql connections
        mysql_engine_string = "mysql://{0}:{1}@{2}/{3}".format(
            mysql_user, mysql_password, mysql_host, mysql_dbname)
        self.mysql_engine = sqlalchemy.create_engine(mysql_engine_string)

    def get_all_responses(self):
        self.data = pd.read_sql(
            "SELECT * FROM kobo ORDER BY uid", self.mysql_engine)

    def get_versions(self):
        self.get_all_responses()
        version_obj = {}

        for index, row_entry in self.data.iterrows():
            row_data = json.loads(row_entry.get("data"))
            form_version = row_data.get("__version__")
            xform_id_string = row_data.get("_xform_id_string")
            asset_name = row_entry.get("asset_name")

            if xform_id_string is None or asset_name is None:
                continue

            if version_obj.get(xform_id_string) is None:
                version_obj[xform_id_string] = {}

            if version_obj[xform_id_string].get(form_version) is None:
                version_obj[xform_id_string][form_version] = []

            if xform_id_strings.xform_id_strings.get(xform_id_string):
                for table in xform_id_strings.xform_id_strings.get(xform_id_string):
                    if form_version in table.get("table_keys") and table.get("table_name") not in version_obj[xform_id_string][form_version]:
                        version_obj[xform_id_string][form_version].append(
                            table.get("table_name"))

        print(version_obj)


fp = FormParser()
fp.get_versions()
