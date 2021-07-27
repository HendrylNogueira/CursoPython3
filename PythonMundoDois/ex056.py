''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade no grupo.
- qual o nome do homem mais velho.
- quantas mulheres tem menos de 20 anos. '''

nome_homem = ''
homem_mais_velho = 0
mulheres_menores = 0
media_idade = 0
for pessoas in range(1, 5):
    print(f'========== {pessoas} PESSOA ==========')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = int(input('[ 1 ] MASCULINO '
                     '[ 2 ] FEMININO'
                     '\nDigite o sexo: '))
    media_idade += idade

    if sexo == 1:
        if pessoas == 1:
            homem_mais_velho = idade
            nome_homem = nome
        else:
            if idade > homem_mais_velho:
                homem_mais_velho = idade
                nome_homem = nome
    if sexo == 2:
        if idade < 20:
            mulheres_menores += 1

print(f'A média de idade do grupo é {media_idade / 4}. ')
print(f'O homem mais velho tem {homem_mais_velho} anos, e seu nome é: {nome_homem}.')
print(f'Nesse grupo tem(os) {mulheres_menores} mulheres com menos de 20 anos. ')
