print('\n***PA COM WHILE***\n')

first = int(input('Digite o primeiro elemento: '))
razao = int(input('Digite a razao: '))

i = 1
add = 1

while add > 0:

	while i  < 10 + add:

		print(f'{first + ((i-1) * razao)}')
		i += 1

	enter = int(input('\nDeseja exibir mais quantos termos? '))
	if enter > 0:
		add += enter
	else:
		add = 0
		break
