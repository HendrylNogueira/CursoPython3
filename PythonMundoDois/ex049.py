'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escoher, só que agora utilizando
um laço for. '''

n2 = 0
n1 = int(input('Digite uma número e veja sua tabuada de 0 a 10: '))
for n in range(0, 11):
    resultado = n1 * n2
    print(f'{n1} x {n2} = {resultado}')
    n2 += 1
