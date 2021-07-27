#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

'''Ou posso usar o comando: from math import floor

O comando "floor" serve para arredondar para baixo, para fazer esse programa
eu poderia ter usado o comando "trunc", que apaga os números após a virgula.'''

import math
n = float(input('Digite um número Real e veja sua porção inteira: '))
print('A porção inteira desse número é: {}'.format(math.floor(n)))
