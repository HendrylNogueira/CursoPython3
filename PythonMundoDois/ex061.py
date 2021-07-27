termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont +=1
print('Fim.')
