''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lita de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista. '''

valores = list()
confirm = ''
cont = 0

while True:
    cont += 1
    valores.append(int(input(f'Digite o {cont}º número: ')))
    confirm = str(input('Deseja continuar? [S/N]: ')).upper()
    while confirm not in 'S' and confirm not in 'N':
        print('Resposta inválida.', end=' ')
        confirm = str(input('Deseja continuar? [S/N]: ')).upper()
    if confirm in 'N':
        break

print(f'Foram digitados {len(valores)} numeros. ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')

if 5 in valores:
    print('O numero cinco foi digitado e está na lista. ', end='')
    print(f'E está na posição {valores.index(5)}')
else:
    print('O numero cinco não for digitado, portanto nao está na lista. ')
