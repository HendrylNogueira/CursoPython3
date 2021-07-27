#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número para ver seu dobro, triplo e raiz quadrada: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O dobro de {} equivale a {};'.format(n, dobro))
print('O triplo de {} equivale a {};'.format(n, triplo))
print('A raiz quadrada de {} equivale a {};'.format(n, raiz))
print('Obrigado pela preferência.')
