import os
from dotenv import load_dotenv
import datetime
from pytz import timezone
import sqlalchemy
import psycopg2
from psycopg2 import sql
import pandas as pd
import json

from parse_forms.assets.asset_names import asset_names

class ListMaker:
    def __init__(self, mode=None):
        load_dotenv()

        date_utc = datetime.datetime.now()
        eastern = timezone('US/Eastern')
        loc_dt = date_utc.astimezone(eastern)
        print("Starting to generate list")
        print(loc_dt)

        self.connect_to_shadow_live()

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
        
    def generate_version_dict(self):
        version_dict = {}

        for asset_name, data in asset_names.items():
            for table in data:
                for version, obj in table.get("table_keys").items():
                    if version_dict.get(version):
                        version_dict[version].append(obj)
                    else:
                        version_dict[version] = []
                        version_dict.get(version).append(obj)
        
        return version_dict

    def generate_editable_list_by_version(self, version_dict):
        editable_list_by_version = {}

        for version, obj in version_dict.items():
            editable_list = []
            for dict_list in obj:
                for row in dict_list:
                    for col in row.get("cols_from_form"):
                        kobo_name = col.get("kobo_name")
                        if kobo_name not in editable_list and kobo_name != "WON'T BE FOUND" and not kobo_name.startswith("_") and "gps" not in kobo_name.lower():
                            editable_list.append(kobo_name)
        
            editable_list_by_version[version] = json.dumps(editable_list)
            
        return editable_list_by_version

    def generate_version_lists(self):
        version_dict = self.generate_version_dict()
        editable_list_by_version = self.generate_editable_list_by_version(version_dict)

        print(editable_list_by_version)

        df = pd.DataFrame(columns=["version", "editable_list"])

        for version, editable_list in editable_list_by_version.items():
            df = df.append({"version": version, "editable_list": editable_list}, ignore_index=True)

        self.convert_to_sql(df)

    def convert_to_sql(self, dataframe):
        dataframe.to_sql("editable_list_by_version", self.shadow_engine, if_exists="replace", index=False)

lm = ListMaker()
lm.generate_version_lists()