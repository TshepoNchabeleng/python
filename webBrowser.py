import webbrowser as wb
import requests

#url_Taylor = "https://www.taylorswift.com/"
#wb.open(f'{url_Taylor}')


""" url_automate = 'https://automatetheboringstuff.com/files/rj.txt'
response = requests.get(f'{url_automate}')
type(response)

response.status_code == requests.codes.ok # you can tell the request for the web page succeeded by checking the status_code
# alternative to check if the download succeeded you can use:
    #response.raise_for_status()
length_text = len(response.text)

print(length_text)
print("*************************")
print(response.text[:210]) """

response = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    response.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')

# Always call raise_for_status() after calling requests.get()