''' Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela. '''

aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] < 6:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print('=' * 50)
for k, v in aluno.items():
    print(f'   - {k} é igual a {v}.')
print('=' * 50)
