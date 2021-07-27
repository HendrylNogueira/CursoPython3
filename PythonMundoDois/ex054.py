''' crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores. '''

from datetime import date
hoje = date. today().year

maior = 0
menor = 0
cont = 0
for c in range(0, 7):
    cont += 1
    nascimento = int(input(f'Digite a {cont}º data de nascimento: '))
    idade = hoje - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'{menor} pessoas ainda são menores de idade. ')
print(f'{maior} pessoas já são maiores de idade. ')
