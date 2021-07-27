'''Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre o status, de acordo com a
tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida.'''

peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / altura ** 2
print(f'Seu IMC é de: {imc:.1f}')
if imc <18.5:
    print(f'Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Voce está com OBESIDADE MÓRBIDA!!')
    print('Procure um médico com urgência')
