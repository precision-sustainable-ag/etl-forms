# to run use 'python -m generate_editable_lists.generate_editable_lists' from ./etl-forms

import os
from dotenv import load_dotenv
import datetime
from pytz import timezone
import sqlalchemy
import psycopg2
from psycopg2 import sql
import pandas as pd
import json
import numpy as np

# from ..parse_forms.assets.asset_names import asset_names
import parse_forms.assets.xform_id_strings as xform_id_strings


class ListMaker:
    def __init__(self, mode=None):
        load_dotenv()

        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        print("Starting to generate list")
        print(loc_dt)

        self.connect_to_shadow_live()
        # self.connect_to_shadow_local()

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

        shadow_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
            postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(shadow_engine_string)

    def connect_to_shadow_live(self):
        postgres_host = os.environ.get('LIVE_SHADOW_HOST')
        postgres_dbname = os.environ.get('LIVE_SHADOW_DBNAME')
        postgres_user = os.environ.get('LIVE_SHADOW_USER')
        postgres_password = os.environ.get('LIVE_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('LIVE_SHADOW_SSLMODE')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
            postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
        # print(postgres_con_string)
        self.shadow_con = psycopg2.connect(postgres_con_string)
        self.shadow_cur = self.shadow_con.cursor()
        self.shadow_con.autocommit = True

        shadow_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(
            postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(shadow_engine_string)

        print("connected to shadow live")

    def generate_version_dict(self):
        version_dict = {}

        for asset_name, data in xform_id_strings.xform_id_strings.items():
            for table in data:
                table_name = table.get("table_name")
                for version, obj in table.get("table_keys").items():
                    if version_dict.get(version):
                        version_dict[version].append([obj, table_name])
                    else:
                        version_dict[version] = []
                        version_dict.get(version).append([obj, table_name])

        return version_dict

    def generate_editable_list_by_version(self, version_dict):
        editable_list_by_version = {
            "version": [],
            "editable_list": [],
            "entry_to_iterate": [],
            "iterator_editable_list": [],
            "table_names": []
        }

        for version, obj in version_dict.items():
            entry_to_iterate = None
            editable_list = []
            iterator_editable_list = []
            version_has_iterator = False
            tables_list = []
            for dict_list_and_table_name in obj:
                tables_list.append(dict_list_and_table_name[1])
                for row in dict_list_and_table_name[0]:
                    if row.get("entry_to_iterate"):
                        entry_to_iterate = row.get("entry_to_iterate")
                        version_has_iterator = True

                    for col in row.get("cols_from_form"):
                        kobo_name = col.get("kobo_name")
                        if kobo_name not in editable_list and kobo_name != "WON'T BE FOUND" and not kobo_name.startswith("_") and "gps" not in kobo_name.lower():
                            if version_has_iterator:
                                iterator_editable_list.append(kobo_name)
                            else:
                                editable_list.append(kobo_name)

            editable_list_by_version["version"].append(version)
            editable_list_by_version["iterator_editable_list"].append(
                json.dumps(iterator_editable_list))
            editable_list_by_version["editable_list"].append(
                json.dumps(editable_list))
            editable_list_by_version["entry_to_iterate"].append(
                entry_to_iterate)
            editable_list_by_version["table_names"].append(
                json.dumps(tables_list))

        return editable_list_by_version

    def generate_version_lists(self):
        version_dict = self.generate_version_dict()
        editable_list_by_version = self.generate_editable_list_by_version(
            version_dict)

        print(editable_list_by_version)

        df = pd.DataFrame(editable_list_by_version)

        df = df.astype(object).where(pd.notnull(df), None)
        print(df)

        self.convert_to_sql(df)

    def convert_to_sql(self, dataframe):
        dataframe.to_sql("editable_list_by_version",
                         self.shadow_engine, if_exists="replace", index=False)


lm = ListMaker()
lm.generate_version_lists()
