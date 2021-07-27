''' Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de vizualização de detalhes
do aproveitamento de cada jogador. '''

todos_jogadores = list()
# ______________________________________________________________________________________________________________________
while True:
    aproveitamento = {'nome': str(input('Digite o nome do jogador: ')),
                      'partidas': [int(input('Digite quantas partidas ele jogou: '))],
                      'gols': []
                      }
    cont = 0
    tot = 0
    while cont <= len(aproveitamento['partidas']):
        cont += 1
        aproveitamento['gols'].append(int(input(f'Digite quantos gols {aproveitamento["nome"]} fez na partida {cont}: ')))
    for c in aproveitamento['gols']:
        tot += c
    aproveitamento['total'] = tot
# ______________________________________________________________________________________________________________________
    continuar = str(input('Quer continuar? [S/N]: '))
    todos_jogadores.append(aproveitamento)
    if continuar in 'Nn':
        break
# ______________________________________________________________________________________________________________________
print('-=' * 40)
print(f'{"cod nome":<18} {"gols":<10} {"total":>20}')
print(f'-' * 50)
cod_nome = 0
for dicionario in todos_jogadores:
    print(f'{cod_nome + 1}     {dicionario["nome"]}     {dicionario["gols"]}     {dicionario["total"]}')
    cod_nome += 1
print('-' * 50)

while True:
    dados_do_jogador = int(input('Mostrar dados de qual jogador? (999 faz parar)'))
    if dados_do_jogador == 999:
        break

    if dados_do_jogador < len(todos_jogadores):
        for dicionario in todos_jogadores:
            for partida in range(0, len(dicionario['partidas'])):
                print(f'No jogo {partida} fez {dicionario["gols"][0:]}')
