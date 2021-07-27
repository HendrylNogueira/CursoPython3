''' Crie um programa que leia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
um dicionário, incluindo o total de gols feitos durante o campeonato. '''

aproveitamento = {'nome': str(input('Digite o nome do jogador: ')),
                  'partidas': int(input('Digite quantas partidas ele jogou: ')),
                  'gols': []
                  }
cont = 0
tot = 0

while cont < aproveitamento['partidas']:
    cont += 1
    aproveitamento['gols'].append(int(input(f'Digite quantos gols {aproveitamento["nome"]} fez na partida {cont}: ')))

for c in aproveitamento['gols']:
    tot += c
aproveitamento['total'] = tot
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)

for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {aproveitamento["nome"]}, jogou {aproveitamento["partidas"]} partidas.')
cont = 0

for c in aproveitamento['gols']:
    cont += 1
    print(f'   => Na partida {cont}, fez {c} gols.')
