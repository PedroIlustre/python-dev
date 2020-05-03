import requests
import json
import hashlib
import time

response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=11721f372b13c7a37a739108ba8ff3d8085bf205')

def decode_letra (letra, numero_casas):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    posicao = alfabeto.find(letra)
    if posicao < 0:
        return letra

    posicao = posicao-numero_casas

    if posicao < 0:
        posicao = len(alfabeto) + posicao

    return alfabeto[posicao]

def decode_frase (frase, numero_casas):
    frase_criptografada = frase.split(' ')
    frase_final = ''
    palavra_final = ''

    for palavra_cripografada in frase_criptografada:
        palavra_final = ''
        for letra in palavra_cripografada:
            palavra_final += (decode_letra(letra, numero_casas))

        frase_final += palavra_final + ' '

    return frase_final

try:
    with open('answer.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

except Exception as erro:
    print('Erro ao Salvar arquivo json:'+format(erro))
    print('Erro Tipo:'+format(type(erro)))

try:
    # Decodifica o texto
    with open('answer.json','r') as arquivo_json:
        dados_json = json.load(arquivo_json)
        frase_final = decode_frase(dados_json['cifrado'], dados_json['numero_casas'])
        dados_json['decifrado'] = frase_final

    # Atualiza o texto decodificado
    with open('answer.json','w') as arquivo_json:
        dados_json = json.dumps(dados_json)
        arquivo_json.write(dados_json)
    time.sleep(2.4)
    # Insere o resumo criptográfico do texto decodificado
    #with open('answer.json','r') as arquivo_json:
    #    dados_json = json.load(arquivo_json)
        

    with open('answer.json','w') as arquivo_json:
        dados_json = json.dumps(dados_json)
        dados_json['resumo_criptografico'] = hashlib.sha1(dados_json['decifrado'].encode()).hexdigest()
        arquivo_json.write(dados_json)
        arquivo_json.close()

except Exception as erro:
    print('Erro ao atualizar arquivo json:'+format(erro))
    print('Erro Tipo:'+format(type(erro)))

