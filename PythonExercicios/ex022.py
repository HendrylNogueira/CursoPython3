#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome do todas as letras minusculas e maiusculas.
#Quantas letras tem ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite sem nome completo: ')).strip()
print(f'Seu nome em maiúsculo fica: {nome.upper()}')
print(f'Seu nome em minúsculo fica: {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(" ")} letras ao todo.')
print(f'Seu primeiro nome tem {nome.find(" ")}')
