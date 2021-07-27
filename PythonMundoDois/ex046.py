'''Faça um programa que mostre na tela uma contagem regrassiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

import time
cont = 10
for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1)
print('BOOOM!! SCABLAUU!!')
print('Parabéns!!')


'''while cont > 0:
    print(cont)
    cont -= 1
Esse é o método para usar o método de repetição 'while'.'''
