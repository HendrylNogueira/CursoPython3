#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''O seno, cosseno e tangente faz a conta em radianos, portanto preciso converter o número para radianos'''

import math

ang = float(input('Digite o ângulo que deseja saber o seno, cosseno e tangente: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f'O seno desse ângulo é: {seno:.2f}')
print(f'O cosseno desse ângulo é: {cosseno:.2f}')
print(f'A tangente desse ângulo é: {tangente:.2f}')
