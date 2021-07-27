''' Escreva um programa que faça o computador "pensar" em um número inteiro enre 0 e 5 e peça para
 o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
 se o usuário venceu ou perdeu. '''

import random
lista = (random.randint(1, 5))
print('Eu pensei em um número de 1 a 5, tente adivinhar! ')
usuario = int(input('Digite um número: '))
print(f'Eu pensei no número {lista}')
if usuario == lista:
    print('Você venceu!!')
else:
    print('Você perdeu...')
