import json
from urllib import request
from wsgiref.util import request_uri

url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
requisicao = request.urlopen(url, timeout=5)
dados = requisicao.read().decode()

cotacao = json.loads(dados)

print('#### Cotação do Dólar ####')
print('Moeda: ' + cotacao['USD']['name'])
print('Dados: ' + cotacao['USD']['create_date'])
print('Valor atual: R$' + cotacao['USD']['bid'])

from asyncio import timeout

request.urlopen(url, data=None, timeout=None, cafile=None, capath=None, cadefault=False, context=None)

requisicao = requisicao = request.urlopen('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()

print('#### Cotação do Dolar ####')

print('Moeda: ' + cotacao['USD']['nome'])

print('Dados: ' + cotacao['USD']['create_date'])

print('Valor atual: R$' + cotacao['USD']['bid'])
