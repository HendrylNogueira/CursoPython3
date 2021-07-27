#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

import random

alu1 = str(input('Digite o nome do primeiro aluno: '))
alu2 = str(input('Digite o nome do segundo aluno: '))
alu3 = str(input('Digite o nome do terceiro aluno: '))
alu4 = str(input('Digite o nome do quarto aluno: '))
lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print(f'A ordem sorteada é: {lista}')
