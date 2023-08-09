import requests

my_lat=33.448376
my_lng = -112.074036
parameters = {
    "lat":my_lat,
    "lon":my_lng,
    "exclude":"current,minutely,daily",
    "appid":"62ec8d22afc1dfb1ecc7b38cbee26382",
}
response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]
pm = []
for inside in weather_data:
    weather_list = inside['weather']
    for weather_dict in weather_list:
        pm.append(weather_dict['id'])
        
for condition_codes in pm:
    if int(condition_codes) < 600:
        print("bring an umbrella")
    else:
        print("you good")


