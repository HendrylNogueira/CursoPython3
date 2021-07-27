''' Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. '''

maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input(f'Digite o {c}º peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'{maior} for o maior peso')
print(f'{menor} foi o menor peso')
