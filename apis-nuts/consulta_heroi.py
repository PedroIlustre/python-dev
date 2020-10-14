import requests
import json

url = 'https://developer.marvel.com/docs'
request = requests.get(url).json()
print(request)