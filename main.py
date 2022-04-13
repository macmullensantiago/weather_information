import requests
from pprint import pprint

API_Key = ''

city = input("Enter a city")

base_url = "http://api.openweathermap.org/date/2.5/weather"+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
