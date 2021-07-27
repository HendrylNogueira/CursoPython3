''' Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiro colocados;
b) Os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense. '''

brasileirao = ('Bragantino', 'Atlético Paranaense', 'Palmeiras', 'Atlético-MG', 'Fortaleza',
               'Santos', 'Bahia', 'Atlético-GO', 'Ceará', 'Fluminense', 'Flamengo', 'Juventude',
               'Corinthians', 'Internacional', 'América-MG', 'Sport Recife', 'São Paulo', 'Cuiabá',
               'Chapecoense', 'Grêmio')
print(f'Os cinco primeiros colocados são: {brasileirao[0:5]}')
print(f'Os últimos 4 colocados são: {brasileirao[-4:]}')
print(f'Em ordem alfabética, fica: {sorted(brasileirao)}')
print(f'A chapecoense está na posição {brasileirao.index("Chapecoense")+1}')
