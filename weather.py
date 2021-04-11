import requests
from elasticsearch import Elasticsearch
from constants import *
from datetime import datetime


if __name__ == "__main__":

    api_onecall_url = '{}?lat={}&lon={}&units=metric&appid={}'.format(weather_onecall_url, athens_lat, athens_lon,
                                                                   weather_api_key)
    r = requests.get(api_onecall_url)

    #r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Athens&units=metric&appid=37f8760f173fb36efa9d6a5ba8a3b705')

    print(r.json())

    daily_forecasts = r.json()['daily']
    hourly_forecasts = r.json()['hourly']

    es = Elasticsearch(cloud_id=cluster_id, http_auth=("elastic", cluster_pwd))

    # mapping = {
    #     "mappings": {
    #         "properties": {
    #             "dt": {
    #                 "type": "date",
    #                 "format": "epoch_second"
    #             }
    #         }
    #     }
    # }

    #response = es.indices.create(index=weather_index, body=mapping)

    for daily_forecast in daily_forecasts:
        # print(daily_forecast)
        es.index(index=weather_index_daily, doc_type='docket', body=daily_forecast)

    for hourly_forecast in hourly_forecasts:
        es.index(index=weather_index_hourly, doc_type='docket', body=hourly_forecast)


