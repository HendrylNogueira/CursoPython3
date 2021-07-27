#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi lugado. Calcule o preço pagar, sabendo que o carro custa R$60,00 o dia e R$0,15 por Km rodado.

tempo = int(input('Por quantos dias o carro ficou alugado? '))
distancia = float(input('Quantos Km foi rodado? '))
valor_diaria = 60 * tempo
valor_por_km = 0.15 * distancia
valor_total = valor_diaria + valor_por_km
print(f'O valor total a seu pago será R${valor_total:.2f}')
