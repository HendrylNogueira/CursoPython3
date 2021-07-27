''' Crie um programa que leia um nome e duas notas de varios alunos e guarde em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente. '''

coisas = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    coisas.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        print('=' * 30)
        print('FINALIZANDO...')
        break
print('=' * 50)
print(F'{"<<< NOTAS DOS ALUNOS >>>":^50}')
print('_' * 50)
print(f'{"Nº":<4}', f'{"ALUNO":<10}', f'{"MÉDIA":>30}')
print(f'-' * 50)
for i, a in enumerate(coisas):
    print(f'{i:<4}', f'{a[0]:<10}', f'{a[2]:>30}')
print(f'-' * 50)
while True:
    consulta = int(input('Digite o índice de um aluno e veja suas notas. (999 para interromper): '))
    if consulta == 999:
        break
    if consulta <= len(coisas) - 1:
        print(f'Notas de {coisas[consulta][0]} são {coisas[consulta][1]}')
