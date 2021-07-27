'''Crie um programa que faça o computador jogar Jokenpô com você.'''

import time
import random
lista = [1, 2, 3]


computador = random.choice(lista)

jogador = int(input('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Digite sua jogada: '''))

time.sleep(0.5)
print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Pô')
time.sleep(0.5)

#coputador vence
if computador == 1 and jogador == 3:
    computador = 'Pedra'
    jogador  = 'Tesoura'
    print(f'O computador venceu')
    print(f'Computador jogou {computador}')
    print(f'Jogador jogou {jogador}')
elif computador == 2 and jogador == 1:
    computador = 'Papel'
    jogador = 'Pedra'
    print(f'O computador venceu')
    print(f'Computador jogou {computador}')
    print(f'Jogador jogou {jogador}')
elif computador == 3 and jogador == 2:
    computador = 'Tesoura'
    jogador = 'Papel'
    print(f'O computador venceu')
    print(f'Computador jogou {computador}')
    print(f'Jogador jogou {jogador}')

#Jogador vence
elif jogador == 1 and computador == 3:
    jogador = 'Pedra'
    computador = 'Tesoura'
    print('O jogador venceu!')
    print(f'O computador jogou {computador}')
    print(f'O jogador jogou {jogador}')
elif jogador == 2 and computador == 1:
    jogador = 'Papel'
    computador = 'Pedra'
    print('O jogador venceu!')
    print(f'O computador jogou {computador}')
    print(f'O jogador jogou {jogador}')
elif jogador == 3 and computador == 2:
    jogador = 'Tesoura'
    computador = 'Papel'
    print('O jogador venceu!')
    print(f'O computador jogou {computador}')
    print(f'O jogador jogou {jogador}')

else:
    print('Empate')
