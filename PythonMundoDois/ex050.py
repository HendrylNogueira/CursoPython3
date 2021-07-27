'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o. '''

soma = 0
cont = 1
for n in range(0, 6):
    numero = int(input(f'Digite o {cont}º valor: '))
    cont += 1
    if numero % 2 == 0:
        soma += numero
print(f'A soma de todos os números pares é igual a {soma}')
