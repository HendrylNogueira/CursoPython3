#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis.

a = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços?', a.isspace())
print('É alfanumérico?', a.isalnum())
print('É alfabético?', a.isalpha())
print('Está em maiúsculo?', a.isupper())
print('Está em minúsculo?', a.islower())
print('Está capitalizada?', a.istitle())
