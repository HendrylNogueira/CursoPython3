'''elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e a condição de pagamento:
- á vista dinheiro ou cheque: 10% de desconto
- á vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros.'''


print(f'{"Lojas HN BLACK":=^40}')

valor = float(input('Qual o valor do produto: R$'))

pagamento = int(input('''[ 1 ] Dinheiro/cheque 
[ 2 ] Cartão
Qual a forma de pagamento: '''))

if pagamento == 2:
    parcelas = int(input('''    [ 1 ] á vista
    [ 2 ] 2x
    [ 3 ] 3x ou mais
    Em quantas parcelas você quer: '''))

    if parcelas == 1:
        desconto = valor * 5 / 100
        print(f'Você tem um desconto de R${desconto:.2f}')
        total = valor - desconto
        print(f'O produto ficou R${total:.2f}')

    elif parcelas == 2:
        print('Você não tem desconto e nem juros.')
        print(f'O pruduto ficou: 2x de R${valor / 2 :.2f}')

    elif parcelas == 3:
        #20% de juros
        quantas_vezes = int(input('Em quantas parcelas vai ser feito: '))
        juros = valor * 20 / 100
        total = valor + juros
        print(f'O produto ficou: {quantas_vezes}x de R${total / quantas_vezes:.2f}')

else:
    #10% desconto
    desconto = valor * 10 / 100
    total = valor - desconto
    print(f'Você tem R${desconto:.2f} de desconto.')
    print(f'O valor total ficou: R${total:.2f}')
