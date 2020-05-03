import requests
import json
import hashlib

response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=11721f372b13c7a37a739108ba8ff3d8085bf205')

def decode_letra (letra, numero_casas):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    posicao = alfabeto.find(letra.lower())
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
        dados_json['decifrado'] = frase_final.strip()

    # Atualiza o texto decodificado
    with open('answer.json','w') as arquivo_json:
        dados_json = json.dumps(dados_json)
        arquivo_json.write(dados_json)

    # Insere o resumo criptográfico do texto decodificado
    with open('answer.json','r') as arquivo_json:
       dados_json = json.load(arquivo_json)
       texto_decifrado = dados_json['decifrado'].encode()
       dados_json['resumo_criptografico'] = hashlib.sha1(texto_decifrado).hexdigest()       

    with open('answer.json','w') as arquivo_json:
        dados_json = json.dumps(dados_json)
        arquivo_json.write(dados_json)
    

    # Envia o arquivo para a url informada
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=11721f372b13c7a37a739108ba8ff3d8085bf205'
    files = {'answer': open('answer.json', 'rb')}
    r = requests.post(url, files=files)
    print(r.content)
        

        
except Exception as erro:
    print('Erro ao atualizar arquivo json:'+format(erro))
    print('Erro Tipo:'+format(type(erro)))

