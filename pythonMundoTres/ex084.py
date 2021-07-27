''' Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

todos = list()
pessoas = list()
peso = list()

while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    todos.append(pessoas[:])
    pessoas.clear()

    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break

for pessoas in todos:
    peso.append(pessoas[1])

print(f'Foram cadastradas {len(todos)} pessoas. ')
print(f'O mais pesado tem {max(peso)} Kg. ')
print(f'O mais leve tem {min(peso)} Kg. ')

''' O exercício foi concluído, mas não com tantos detalhes. '''
