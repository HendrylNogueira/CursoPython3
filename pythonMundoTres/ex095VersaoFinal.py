todos = list()
while True:
    cont = 0
    jogadores = {'nome': str(input('Digite o nome do jogador: ')),
                 'partidas': int(input('Quantas partidas ele jogou: ')),
                 'gols': []}
    while cont < jogadores['partidas']:
        cont += 1
        jogadores['gols'].append(int(input(f'Quantos gols ele fez na {cont} partida: ')))

    todos.append(jogadores.copy())
    jogadores.clear()
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break

print('-=' * 40)
print(f'{"cod nome":<18} {"gols":<10} {"total":>40}')
print(f'-' * 70)
cod_nome = 0
for dicionario in todos:
    print(f'{cod_nome} ', end='')
    print(f'{dicionario["nome"]:<17}', end='')
    print(f'{str(dicionario["gols"]):<10}', end='')
    print(f'{sum(dicionario["gols"]):>40}')
    cod_nome += 1
print('-=' * 40)
while True:
    detalhes = int(input('Mostrar dados de qual jogador? (999 faz parar) '))
    if detalhes == 999:
        break
    elif detalhes <= cod_nome:
        print(f' -- LEVANTAMENTO DO JOGADOR {todos[detalhes]["nome"]}:')
        for i, g in enumerate(todos[detalhes]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    else:
        print('Erro, número inválido.')
