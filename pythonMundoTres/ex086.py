''' Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta. '''

lista = [[], [], []]
coluna = 0
linha = 0
for linha1 in range(0, 3):
    lista[0].append(int(input(f'Digite o valor para ({linha}, {coluna}): ')))
    coluna += 1

coluna = 0
for linha2 in range(0, 3):
    lista[1].append(int(input(f'Digite o valor para ({linha + 1}, {coluna}): ')))
    coluna += 1

coluna = 0
for linha3 in range(0, 3):
    lista[2].append(int(input(f'Digite o valor para ({linha + 2}, {coluna}): ')))
    coluna += 1

print('-=' * 30)
for c in lista[0]:
    print(f'[{c:^5}]', end='')
print()
for c in lista[1]:
    print(f'[{c:^5}]', end='')
print()
for c in lista[2]:
    print(f'[{c:^5}]', end='')
print()
