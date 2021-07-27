#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Digite aqui a altura da parede que deseja pintar: '))
largura = float(input('Digite aqui a largura da parede que deseja pintar:'))
area = altura * largura
quantidade_tinta = area / 2
print(f'Considerando a altura e a largura informada, temos uma área de {area} metros².')
print(f'Será necessário {quantidade_tinta} litros de tinta para pintar essa parede.')
