import requests
import json

response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=11721f372b13c7a37a739108ba8ff3d8085bf205')

def decode_letra (letra, numero_casas):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    posicao = alfabeto.find(letra)
    posicao = posicao-numero_casas

    if posicao < 0:
        posicao = len(alfabeto) + posicao

    return alfabeto[posicao]

def decode_frase (frase, numero_casas):
    frase_criptografada = frase.split(' ')
    frase_final = ''
    palavra_final = ''
    palavra_cript = ''

    for palavra_cripografada in frase_criptografada:
        for ins,letra in palavra_cripografada:
            palavra_cript = palavra_cript + (decode_letra(letra, numero_casas))
            print(palavra_cript)
        palavra_final = palavra_final + palavra_cript

    return frase_final

try:
    with open('answer.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

except Exception as erro:
    print('Erro ao Salvar arquivo json:'+format(erro))
    print('Erro Tipo:'+format(type(erro)))

try:
    arquivo_json = open('answer.json','r')
    dados_json = json.load(arquivo_json)
    frase_final = decode_frase(dados_json['cifrado'], dados_json['numero_casas'])
    print(frase_final)

except Exception as erro:
    print('Erro ao abrir arquivo json:'+format(erro))
    print('Erro Tipo:'+format(type(erro)))

