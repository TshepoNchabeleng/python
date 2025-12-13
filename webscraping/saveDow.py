import requests

url_automate = 'https://automatetheboringstuff.com/files/rj.txt'
response = requests.get(f'{url_automate}')
response.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as play_file:
    for chunk in response.iter_content(100000):
        play_file.write(chunk)

