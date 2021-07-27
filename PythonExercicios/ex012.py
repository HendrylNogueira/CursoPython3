#Faça um algoritimo que leia o preço de um pruduto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o valor do produto: R$'))
desconto = preco * 5 / 100
novo_preco = preco - desconto
print(f'Você tem direito a R${desconto:.2f} de desconto.')
print(f'O valor final do produto ficou R${novo_preco:.2f}')
print('Tenha um bom dia, e volte sempre!')
