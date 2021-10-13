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


class Resetter:
    def __init__(self):
        load_dotenv()
        self.connect_to_shadow_local()
        print("connected to db")

        self.tables = [
            "gps_corners__gps",
            "wsensor_install__water_sensor_install",
            "decomp_biomass_fresh__decomp_bag_pre_wt",
            "decomp_biomass_fresh__biomass_decomp_bag",
            "decomp_biomass_dry__decomp_bag_dry_wt",
            "decomp_biomass_dry__decomp_bag_collect",
            "biomass_in_field__biomass_decomp_bag",
        ]

    # def connect_to_shadow_live(self):
    #     postgres_host = os.environ.get('POSTGRESQL_SHADOW_HOST')
    #     postgres_dbname = os.environ.get('POSTGRESQL_SHADOW_DBNAME')
    #     postgres_user = os.environ.get('POSTGRESQL_SHADOW_USER')
    #     postgres_password = os.environ.get('POSTGRESQL_SHADOW_PASSWORD')
    #     postgres_sslmode = os.environ.get('POSTGRESQL_SHADOW_SSLMODE')

    #     # Make postgres connections
    #     postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode)
    #     self.shadow_con = psycopg2.connect(postgres_con_string)
    #     self.shadow_cur = self.shadow_con.cursor()
    #     self.shadow_con.autocommit = True

    #     postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(postgres_user, postgres_password, postgres_host, postgres_dbname)
    #     self.shadow_engine = sqlalchemy.create_engine(postgres_engine_string)

    def connect_to_shadow_local(self):
        postgres_host = os.environ.get('LOCAL_SHADOW_HOST')
        postgres_dbname = os.environ.get('LOCAL_SHADOW_DBNAME')
        postgres_user = os.environ.get('LOCAL_SHADOW_USER')
        postgres_password = os.environ.get('LOCAL_SHADOW_PASSWORD')
        postgres_sslmode = os.environ.get('LOCAL_SHADOW_SSLMODE')
        postgres_port = os.environ.get('LOCAL_SHADOW_PORT')

        # Make postgres connections
        postgres_con_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(postgres_host, postgres_user, postgres_dbname, postgres_password, postgres_sslmode, postgres_port)
        self.shadow_con = psycopg2.connect(postgres_con_string)
        self.shadow_cur = self.shadow_con.cursor()
        self.shadow_con.autocommit = True

        postgres_engine_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(postgres_user, postgres_password, postgres_host, postgres_port, postgres_dbname)
        self.shadow_engine = sqlalchemy.create_engine(postgres_engine_string)

        print("Connected to shadow local")

    def close_cons(self):
        self.shadow_con.close()

    def push_to_prod(self):
        for table in self.tables:
            unpushed_rows = pd.DataFrame(pd.read_sql("SELECT * FROM {}".format(table), self.shadow_engine))

            # for index, row_entry in unpushed_rows.iterrows():
            update_sql_string = "UPDATE {table} SET pushed_to_prod = 0"
            update_query = sql.SQL(update_sql_string).format(
                table=sql.Identifier(table),
            )

            try:
                self.shadow_cur.execute(update_query)
                self.shadow_con.commit()
            except Exception:
                print("error")
                print(traceback.print_exc(file=sys.stdout))

r = Resetter()
r.push_to_prod()
r.close_cons()