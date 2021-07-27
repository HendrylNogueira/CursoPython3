#Faça um programa que leia o comprimento do cateto oposto e doa cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.
#import math
from math import sqrt
cat_adja = float(input('Digite o valor do cateto adjacente: '))
cat_opos = float(input('Digite o valor do cateto oposto: '))
hipot = cat_opos ** 2 + cat_adja ** 2
hipotenusa = sqrt(hipot)
print(f'O comprimento da hipoteenusa é {hipotenusa:.2f}')
