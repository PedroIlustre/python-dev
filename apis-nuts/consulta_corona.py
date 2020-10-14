import requests
import json

url = 'https://corona.lmao.ninja/v2/countries/brazil'
request = requests.get(url).json()
print(request['country'])