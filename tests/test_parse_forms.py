# python -m tests.test_parse_forms

from parse_forms.parse_forms import FormParser
from parse_forms.api_calls import get_active_farm_codes
from parse_forms.api_calls import get_producers

import traceback
import sys
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
import sqlalchemy


class Tester:
    def __init__(self, errors_object):
        load_dotenv()
        self.connect_to_mysql()
        self.connect_to_shadow_live()

        self.errors_object = errors_object

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

        live_postgres_engine_string = "postgresql://{0}:{1}@{2}/{3}".format(
            postgres_user, postgres_password, postgres_host, postgres_dbname)
        self.live_postgres_engine = sqlalchemy.create_engine(
            live_postgres_engine_string)

    def connect_to_mysql(self):
        mysql_host = os.environ.get('MYSQL_HOST')
        mysql_dbname = os.environ.get('MYSQL_DBNAME')
        mysql_user = os.environ.get('MYSQL_USER')
        mysql_password = os.environ.get('MYSQL_PASSWORD')

        # Make mysql connections
        mysql_engine_string = "mysql://{0}:{1}@{2}/{3}".format(
            mysql_user, mysql_password, mysql_host, mysql_dbname)
        self.mysql_engine = sqlalchemy.create_engine(mysql_engine_string)

    def close_con(self):
        self.postgres_con.close()

    def fetch_kobo_data(self, uid):
        data = pd.read_sql(
            "SELECT * FROM kobo WHERE uid = {}".format(uid), self.mysql_engine)

        return data

    def fetch_shadow_data(self, uid, table_name):
        data = pd.read_sql(
            "SELECT * FROM {} WHERE rawuid = {}".format(table_name, uid), self.live_postgres_engine, parse_dates=True)

        return data

    def call_api(self):
        self.active_farm_codes = get_active_farm_codes.create_years_object()
        self.valid_producers = get_producers.create_producers_object()

    def test_data(self, uid):
        data = self.fetch_kobo_data(uid)

        fp = FormParser("local", True, data,
                        self.active_farm_codes, self.valid_producers)

        dataframe_obj = fp.parse_forms()

        for table in dataframe_obj["valid"]:
            shadow_data = self.fetch_shadow_data(uid, table["table_name"])
            table_data = table["dataframe"]

            if shadow_data.empty:
                continue

            shadow_data = shadow_data.drop(
                columns=['parsed_at', 'pushed_to_prod', 'sid', 'notes', 'submitted_by']).sort_index(axis=1)
            table_data = table_data.drop(
                columns=['parsed_at', 'pushed_to_prod', 'notes', 'submitted_by']).sort_index(axis=1).astype(shadow_data.dtypes.to_dict())

            outer_join = shadow_data.merge(
                table_data, how='outer', indicator=True)

            anti_join = outer_join[~(outer_join._merge == 'both')].drop(
                '_merge', axis=1)

            if not anti_join.empty:
                shadow_json = shadow_data.to_json(orient="records")
                table_json = table_data.to_json(orient="records")

                if shadow_json != table_json:
                    print("error parsing " + table["table_name"])

                    self.errors_object['uid'].append(uid)
                    self.errors_object['shadow_data'].append(shadow_json)
                    self.errors_object['table_data'].append(table_json)
                    self.errors_object['table_name'].append(
                        table["table_name"])

            table["dataframe"] = pd.DataFrame

        fp.empty_dataframes()

        self.close_con()

    def return_errors_obj(self):
        return errors_object


try:
    errors_object = {
        "uid": [],
        "shadow_data": [],
        "table_data": [],
        "table_name": [],
    }

    t = Tester(errors_object)
    t.call_api()
    for i in range(0, 2200):
        t.test_data(i)

    errors_df = pd.DataFrame(t.return_errors_obj())
    errors_df.to_excel('errors.xlsx')

except Exception:
    print("A general error ocurred \n")
    print(traceback.print_exc(file=sys.stdout))
