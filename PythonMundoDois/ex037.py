''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário qual
será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número para ter sua converção: '))
print('''Escolha uma das bases para converção:
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
base = int(input('Para qual base vc quer efetuar  converção? '))
if base == 1:
    print(f'{num} número convertido para BINARIO é igual a: {bin(num)[2:]}')
elif base == 2:
    print(f'{num} número convertido para OCTAL é igual a: {oct(num)[2:]}')
elif base == 3:
    print(f'{num} número convertido para HEXADECIMAL é igual a: {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
