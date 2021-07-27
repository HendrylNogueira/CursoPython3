''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas. xxxxxxx
B) A média de idade do grupo.     xxxxxxxx
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média. '''

lista_de_tudo = list()
mulheres = list()
while True:
    dados = {'nome': str(input('Digite o nome: ')),
             'sexo': str(input('Digite o sexo [M/F]: ')),
             'idade': int(input('Digite a idade: ')),
             }
    lista_de_tudo.append(dados.copy())
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break

soma_de_idade = 0
print('-=' * 30)
for dicionario in lista_de_tudo:
    soma_de_idade += dicionario['idade']

print(f'Foram cadastradas {len(lista_de_tudo)} pessoas. ')
print(f'A média de idade é {soma_de_idade / len(lista_de_tudo)}')
print('As mulheres cadastradas foram: ', end='')
for dicionario in lista_de_tudo:
    if dicionario['sexo'] in 'Ff':
        print(f"{dicionario['nome']} ", end='')
print()
print(f'Lista de pessoas que estão acima da média de idade:')
for dicionario in lista_de_tudo:
    if dicionario['idade'] > (soma_de_idade / len(lista_de_tudo)):
        print()
        print(f'Nome = {dicionario["nome"]}; sexo = {dicionario["sexo"]}; idade = {dicionario["idade"]}')
print('<<< ENCERRADO >>>')
