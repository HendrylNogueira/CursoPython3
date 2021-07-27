'''Escreva um programa para aprovar um emprestimo bancário para comprar uma casa.
Pergunte o valor da casa, o salário so comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exeder 30% do salário ou então o emprestimo será negado.'''

import time

valor = float(input('Digite  valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
quantidade_de_prestacoes = int(input('Digite em quantas vezes ele quer pagar: '))
valor_prestacao = valor / quantidade_de_prestacoes

time.sleep(1)
print('Processando dados')
time.sleep(2)
print('...')
time.sleep(3)

if valor_prestacao > salario * 30 / 100:
    print('O emprestimo foi negado.')
else:
    print('O emprestimo foi aprovado.')
