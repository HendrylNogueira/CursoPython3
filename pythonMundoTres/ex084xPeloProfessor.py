temporaria = list()
principal = list()
maior = menor = 0
while True:
    temporaria.append(str(input('Digite o nome: ')))
    temporaria.append(float(input('Digite o peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print('-=' * 30 )
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
