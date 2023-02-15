#Verifica entre 7 pessoas quantas sao maiores de idade
from datetime import datetime

print('\n***É MAIOR DE IDADE?***\n')

hoje = datetime.now().date().year

maior = 0
menor = 0

qtde = int(input('Quantas pessoas quer analizar? '))

for c in range(1, qtde + 1):

	age = int(input(f'\nDigite o ano de nascimento da {c}° pessoa: '))

	if hoje - age >= 18:

		maior += 1
	else:
		menor += 1

print(f'''\nDas {maior + menor} pessoas:

{maior} sao maiores de idade
{menor} sao menores de idade\n''')
