''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais. '''

palavras = ('Computador', 'Mesa', 'Escrivaninha', 'Celular', 'Cortina', 'Caderno', 'Caneta', 'Azul', 'Amarelo')
print('=' * 60)
for pos in palavras:
    print(f'\nNa palavra "{pos.upper()}"', end=' ')
    print('Temos as vogais: ', end='')
    for p in pos:
        if p in 'a e i o u':
            print(f'{p[0]}', end='-')
    print(' Fim')
#print('')
print('=' * 60)
