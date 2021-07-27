''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que está na tupla. '''
import random

num = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'Os valores sorteados foram: {num}')
print(f'O maior valor é {max(num)}')
print(f'O menor valor é {min(num)}')
