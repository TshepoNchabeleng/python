import os
from dotenv import load_dotenv
import requests
import json

city_name = 'Pretoria'
state_code = 'GP'
country_code = 'ZA'
API_key = os.getenv("MY_WEATHER_API")
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
response.text

response_data = json.loads(response.text)
response_data

print(response_data)