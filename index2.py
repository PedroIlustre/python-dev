import requests
import json
response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=11721f372b13c7a37a739108ba8ff3d8085bf205')

print (response.content)
