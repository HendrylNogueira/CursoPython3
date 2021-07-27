valores = list()
c = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {c + 1} valor: ')))
    c += 1
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
