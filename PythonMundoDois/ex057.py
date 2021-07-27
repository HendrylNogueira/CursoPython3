''' Faça um programa que leia o sexo de um pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto. '''


sexo = str(input('Seu sexo é " M / F ": ')).upper()
while sexo not in 'M' and sexo not in 'F':
    print('Resposta inválida. ')
    sexo = str(input('Seu sexo é " M / F ": ')).upper()
