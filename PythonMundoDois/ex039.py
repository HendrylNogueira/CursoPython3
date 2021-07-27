'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda
vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou da hora se alistar.
Seu programa também deverá mostrar o tempo que ainda falta ou que já passou do prazo.
'''

from datetime import date

data_atual = date.today().year
ano = int(input('Digite, em que ano você nasceu:'))
idade = data_atual - ano
if idade < 18:
    print(f'Você tem {idade} anos.')
    print(f'Ainda falta {18 - idade} anos para o seu alistamento')
elif idade == 18:
    print(f'Você tem {idade} anos! ')
    print(f'Deve se alistar esse ano')
else:
    print(f'Você tem {idade} anos.')
    print(f'Você deveria ter se alistado a {idade - 18} anos atras.')
    print('Aliste-se IMEDIATAMENTE.')
