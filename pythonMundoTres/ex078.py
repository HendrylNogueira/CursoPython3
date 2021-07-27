''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qua foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = list()
for cont in range(1, 6):
    valores.append(int(input(f'Digite o {cont}º número: ')))

print('-=' * 30)
maior = max(valores)
menor = min(valores)
print(f'Você digitou ou valores {valores}')
print(f'O maior valor é {max(valores)}, e está na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor é {min(valores)}, e está na posição: ', end='')
for o, j in enumerate(valores):
    if j == menor:
        print(f'{o}...', end='')
print('\nFim do projeto. ')
