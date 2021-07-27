''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar (considerando 35 anos de contribuição). '''

from datetime import *
ano_atual = date.today().year

dados = {'nome': str(input('Digite seu nome: ')),
         'nascimento': int(input('Digite sua data de nascimento: ')),
         'CTPS': int(input('Digite o nº da sua CTPS: (0 não tem)'))
         }
dados['idade'] = ano_atual - dados['nascimento']
if dados['CTPS'] > 0:
    dados['data de contratação'] = int(input('Digite seu ano de contratação: '))
    dados['salário'] = float(input('Digite o seu salário: '))
    dados['vai se aposentar'] = dados['data de contratação'] + 35

print('-=' * 30)
for k, v in dados.items():
    if k and v != dados['nascimento']:
        print(f'{k} tem o valor {v}')
