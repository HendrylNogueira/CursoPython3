#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

print('Esse programa converte metros para centimetros e milimetros.')
medida = float(input('Digite quantos metros você quer converter: '))
centimetros = medida * 100
milimetros = medida * 1000
print('{} metros equivalem a {} centimetros e a {} milimetros.'.format(medida, centimetros, milimetros))
