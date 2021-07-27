''' Crie um programa onde o usuario possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número ja exista la dentro, ele não será adicionado.
No final, todos os valores unicos digitatos, em ordem crescente. '''

lista = list()
pos = 1
continuar = ' '
while True:
    listanum = int(input(f'Digite o {pos}º valor: '))
    if listanum in lista:
        print('Valor duplicado!, Esse valor não será adicionado')
    else:
        lista.append(listanum)
    pos += 1
    continuar = str(input('Quer continuar? [S/N]')).upper()
    while continuar not in 'SN':
        print('Comando inválido.')
        continuar = str(input('Quer continuar? [S/N]')).upper()
    if continuar in 'S':
        continue
    if continuar in 'N':
        break
print('Fim do programa. ')
print(f'Você digitou os valores: {lista}')
