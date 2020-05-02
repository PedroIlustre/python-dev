import requests
import json

response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=11721f372b13c7a37a739108ba8ff3d8085bf205')

try:
    arquivo_json = open("answer.json","wb")
    arquivo_json.write(response.content)
    arquivo_json.close()

except Exception as erro:
    print('Erro:'+format(erro))
    print('Erro Tipo:'+format(type(erro)))