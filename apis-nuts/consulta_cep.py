import requests
import json

cep_input = input('Digite, com 8 digitos um cep para consulta: ')

if len(cep_input) > 8:
    print('Valor informado acima do esperado')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

addres_data = request.json()

print(addres_data)
