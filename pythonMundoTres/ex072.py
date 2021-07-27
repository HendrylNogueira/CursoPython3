''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0, 20) e mostrá-lo por extenso. '''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20: '))
while True:
    if num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número de 0 a 20: '))
    else:
        break
print(f'Você digitou o número {numeros[num]}.')
