''' Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados corretamente. '''
import requests
from tkinter import *


def rodar_programa():
    parenteses_abertos = list()
    parenteses_fechados = list()

    expressao = str(input('Digite a expressão: '))

    for c in expressao:
        if c in '(':
            parenteses_abertos.append('(')
        elif c in ')':
            parenteses_fechados.append(')')

    if len(parenteses_abertos) == len(parenteses_fechados):
        print('A expressão está correta! ')
    else:
        print('A expressão está incorreta. ')

'''    texto_programa['text'] = expressao

janela = Tk()
janela.title('Verificador de Expressões Matemáticas')


texto_orientacao = Label(janela, text='Clique no botão para iniciar o programa')
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text='Rodar programa.', command=rodar_programa)
botao.grid(column=0, row=1)

texto_programa = Label(janela, text='')
texto_programa.grid(column=0, row=2)


janela.mainloop()
'''
# Não consegui criar um janela ainda.
