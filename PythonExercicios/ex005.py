#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))
ante = numero - 1
suce = numero + 1
print('Analizando o número {}, seu antecessor é {} e seu sucessor é {}'.format(numero, ante, suce))
