''' Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram nescessários
para vencer. '''

import random
import time

cont = 1

lista = (random.randint(0, 10))
print('Eu pensei em um número de 0 a 10, tente adivinhar! ')
usuario = int(input('Digite um número: '))
print('\033[31mProcessando...\033[m')
time.sleep(2)
while usuario != lista:
    cont += 1
    print('Quase lá! Tente novamente.')
    usuario = int(input('Digite um número: '))
    print('\033[31mProcessando...\033[m')
    time.sleep(2)
print(f'\033[33mParabéns! você acertou.\033[m')
print(f'Você precisou de {cont} jogadas para acertar. ')
