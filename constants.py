directory = '/home/nikmand/Downloads/ubitech_tech_challenge'
index_name = "datamodel"
cluster_id = "i-o-optimized-deployment:ZnJhbmNlY2VudHJhbC5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDllYjIzOTc4ZDE0NDQ2ODM5NjIzZDQ1YTRmMzhlMmM4JDdiYzQ0ZTI3MzBjMzQzN2RiN2FjYzUxMWIyZTdhNTFj"
cluster_pwd = "92G8QuO5mR0NlWEWl33CxrE6"

common_time_field = "commonTimeField"

# for each type specifies which time field is representative of the event
mappings = {
    "Building": "createdAt",
    "BuildingOperation": "createdAt",
    "Battery": None,
    "BatteryStatus": "dateObserved",
    "StorageBatteryDevice": "dateLastReported",
    "PhotovoltaicDevice": "dateLastReported",
    "PhotovoltaicMeasurement": "dateObserved",
    "InverterDevice": "dateLastReported",
    "WeatherForecast": "dateIssued",
    "WeatherObserved": "dateObserved"
}

athens_lon = 23.72
athens_lat = 37.98

weather_api_key = "37f8760f173fb36efa9d6a5ba8a3b705"
weather_onecall_url = "https://api.openweathermap.org/data/2.5/onecall"

weather_index_daily = "weather_daily"
weather_index_hourly = "weather_hourly"
