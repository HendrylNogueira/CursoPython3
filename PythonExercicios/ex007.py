#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Considerando que sua primeira nota foi {}, e sua segunda nota foi {}:'.format(nota1, nota2))
print('Sua média atingiu {}'.format(media))
