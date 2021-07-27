''' Crie um programa que vai ler vários numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas. '''

lista1 = list()
lista_par = list()
lista_impar = list()

while True:
    lista1.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar in 'N':
        break

for num in lista1:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f'A lista completa é: {lista1}')
print(f'Os valores pares são: {lista_par}')
print(f'Os valores ímpares são: {lista_impar}')
