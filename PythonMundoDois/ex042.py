'''Refaça o desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
Escaleno: todos os lados diferentes.'''

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos formam um triângulo! ')
    if r1 == r2 and r1 == r3 and r2 == r1 and r2 == r3 and r3 == r1 and r3 == r2:
        print('Esse é um triângulo Equilátero')
    elif r1 != r2 and r1 != r3 and r2 != r1 and r2 != r3 and r3 != r1 and r3 != r2:
        print('Esse é um triângulo escaleno. ')
    else:
        print('Esse é um triângulo Isósceles')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')
