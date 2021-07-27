''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_dos_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda = []

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_dos_pares += matriz[l][c]
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
        if l == 1:
            maior_valor_segunda.append(matriz[l][c])

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 50)
print(f'A soma dos valoress pares é: {soma_dos_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {max(maior_valor_segunda)}')
print('=' * 50)
