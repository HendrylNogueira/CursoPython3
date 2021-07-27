#Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite qual é o seu salário: R$'))
aumento = salario * 15 / 100
novo_salario = salario + aumento
print(f'Com base no seu salário, você recebeu R${aumento:.2f} de aumento.')
print(f'Seu salário atual é de R${novo_salario:.2f}')
print('Continue se esforçando e trabalhando cada vez mais, para que seu salário aumente novamente!')
