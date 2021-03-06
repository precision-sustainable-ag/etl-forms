import http.client	
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_connection = http.client.HTTPSConnection("api.precisionsustainableag.org")
YEARS = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
YEARS_OBJECT = {}

def get_farms(year):
    api_key = os.environ.get('X_API_KEY')

    api_headers = { "x-api-key": api_key}
    uri = "/onfarm/raw?table=site_information&year={}&options=showtest".format(year)

    # print(uri)

    api_connection.request("GET", uri, headers=api_headers)	

    api_res = api_connection.getresponse()	
    api_data = api_res.read()
    # convert to json	
    json_api_data = api_data.decode('utf8')	
    api_json_data = json.loads(json_api_data)

    # print(api_json_data)
    return(api_json_data)

def create_object(data, year):
    YEARS_OBJECT[year] = {}
    for farm in data:
        YEARS_OBJECT[year][farm.get("code")] = True

def create_years_object():
    for year in YEARS:
        data = get_farms(year)
        create_object(data, year)

    # print(YEARS_OBJECT)
    return YEARS_OBJECT

create_years_object()