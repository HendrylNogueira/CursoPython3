'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO. '''

nota1= float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota2 + nota1) / 2
print(f'Sua média final é {media}')
if media < 5:
    print('Você está reprovado!')
elif media > 5 and media < 6.9:
    print('Você está de recuperação.')
    print('Estude mais')
else:
    print('Parabens!')
    print('Você está aprovado!')
