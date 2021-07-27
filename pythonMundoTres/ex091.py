''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados alestórios. Guarde esses resultados em
um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. '''

from random import *
from time import *
from operator import *

jogadores = dict()
ranking = dict()
cont = 1
for j in range(1, 5):
    jogadores[f'Jogador{j}'] = randint(1, 6)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for k, v in jogadores.items():
    print(f'{k} = {v}')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==  ')
for k, v in ranking:
    print(f'   {cont}º lugar: {k} com {v}.')
    cont += 1
    sleep(1)
