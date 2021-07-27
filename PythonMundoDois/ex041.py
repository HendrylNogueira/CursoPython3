'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirin
- até 14 anos: infantil
- até 19 anos: junior
- até 25 anos: senior
- acima: master'''

from datetime import date
ano = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano - nascimento
if idade <= 9:
    print(f'Você tem {idade} anos.')
    print('Classificação: Mirin')
elif idade <= 14:
    print(f'Você tem {idade} anos.')
    print('Classificação: Infantil ')
elif idade <= 19:
    print(f'Você tem {idade} anos.')
    print('Classificação: Junior ')
elif idade <= 25:
    print(f'Você tem {idade} anos. ')
    print('Cassificação Senior')
else:
    print(f'Você tem {idade} anos. ')
    print('Classificação: Master')
