import http.client	
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_connection = http.client.HTTPSConnection("api.precisionsustainableag.org")
YEARS = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
# YEARS_OBJECT = {}

def get_producers():
    api_key = os.environ.get('X_API_KEY')

    api_headers = { "x-api-key": api_key}
    uri = "/onfarm/producers?output=json"

    # print(uri)

    api_connection.request("GET", uri, headers=api_headers)	

    api_res = api_connection.getresponse()	
    api_data = api_res.read()
    # convert to json	
    json_api_data = api_data.decode('utf8')	
    print(json_api_data)
    api_json_data = json.loads(json_api_data)

    # print(api_json_data)
    return(api_json_data)

def create_object(data):
    producers_object = {}
    for producer in data:
        producers_object[producer.get("email")] = producer.get("producer_id")
        producers_object[producer.get("phone")] = producer.get("producer_id")

    return producers_object

def create_producers_object():
    data = get_producers()
    producers_object = create_object(data)
    # print(producers_object)

    # print(YEARS_OBJECT)
    return producers_object

# create_years_object()