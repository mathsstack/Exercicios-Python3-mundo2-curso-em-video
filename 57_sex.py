#Valida o sexo de um usuário

print('\n***VALIDACAO DE SEXO***\n')

erro = 1

while erro == 1:

	choice = input('Escolha M para masculino ou F para feminino: ')

	if choice == 'M' or choice == 'F':
		erro = 0
	else:
		print('\n\033[33mENTRADA INVÁLIDA\033[m')
