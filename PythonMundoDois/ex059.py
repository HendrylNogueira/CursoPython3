''' Crie um programa que leia dois valores e mostre um menu como o abaixo:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa '''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resposta = 0
maior = 0
while resposta != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa ''')
    resposta = int(input('O que você deseja fazer: '))
    if resposta == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif resposta == 2:
        produto = n1 * n2
        print(f'O resultado entre {n1} x {n2} é {produto}')
    elif resposta == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}. ')
        else:
            print(f'O maior valor é {n2}. ')
    elif resposta == 4:
        print('informe outros valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif resposta == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
print('Fim do programa volte sempre. ')
