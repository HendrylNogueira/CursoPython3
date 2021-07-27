'''Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram
no intervalo de 1 até 500. '''

cont = 0
total = 0
for soma in range(1, 501, 2):
    if soma % 3 == 0:
        cont += 1
        total += soma
print(f'Foram encontrados {cont} valores coma as características especificadas.')
print(f'E a soma deles é igual a {total}')
