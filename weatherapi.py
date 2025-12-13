import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

city_name = 'Pretoria'
state_code = 'GP'
country_code = 'ZA'
API_key = os.getenv("MY_WEATHER_API")
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
response.text

response_data = json.loads(response.text)
response_data
print(API_key)
try:
    print(response_data)
    
except HTTPError as e:
    if response.status_code == 401:
        print(f"Error: {response.status_code} Invalid API key")