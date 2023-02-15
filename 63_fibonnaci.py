print('\n***SEQUENCIA DE FIBONNACI***\n')

qtde = int(input('Quantos termos quer imprimir? '))

i = 1
first = 0
second = 1

while i < qtde + 1:

	if i % 2 != 0:

		print(f'{first}')
		i += 1
	elif i % 2 == 0:

		print(f'{second}')


		first += second
		second += first
		i += 1
