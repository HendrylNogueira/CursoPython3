#Crie um programa que leia quanto dinheiro uma pessoa em na carteira e mostre quantos dólares ela pode comprar.

din = float(input('Digite quantos reais você tem a sua carteira: R$'))
dolar = din / 3.27
print(f'Com R${din:.2f} você pode comprar US${dolar:.2f}')

