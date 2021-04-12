import requests
from elasticsearch import Elasticsearch
from constants import *
from datetime import datetime


if __name__ == "__main__":

    api_onecall_url = '{}?lat={}&lon={}&units=metric&appid={}'.format(weather_onecall_url, athens_lat, athens_lon,
                                                                      weather_api_key)
    response = requests.get(api_onecall_url).json()

    daily_forecasts = response['daily']

    daily_forecasts["dt"] = datetime.fromtimestamp(daily_forecasts["dt"])

    es = Elasticsearch(cloud_id=cluster_id, http_auth=("elastic", cluster_pwd))

    for daily_forecast in daily_forecasts:
        es.index(index=weather_index_daily, doc_type='docket', body=daily_forecast)
