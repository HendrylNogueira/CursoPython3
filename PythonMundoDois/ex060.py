''' Faça um programa que leia um número qualquer, e mostre o seu fatorial. '''

num = int(input('informe um valor: '))
cont = num
f = 1
while cont > 0:
    print(f'{num} x {cont}')
    f *= cont
    cont -= 1
print(f)
