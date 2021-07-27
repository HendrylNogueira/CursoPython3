'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais. '''

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 > valor2:
    print(f'O valor {valor1} é maior do que {valor2}.')
elif valor2 > valor1:
    print(f'O valor {valor2} é maior do que {valor1}')
else:
    print(f'Não existe valor maior ou menor, os dois valores são iguais.')
