#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

celsius = float(input('Digite sua temperatura em ºC: '))
fahrenheit = (celsius * 1.8) + 32
print(f'Sua temperatura equivale a {fahrenheit}ºF.')
