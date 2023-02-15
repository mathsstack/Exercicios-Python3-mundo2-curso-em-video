#verifica se alguem pode financiar uma casa

print('\n***CALCULADORA DE EMPRESTIMOS***\n')

valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
tempo = float(input('Em quantos anos pretende pagar? '))

prestacao = valorcasa / (tempo * 12)

if prestacao > salario * 0.3:

	print('\n\033[1;31mVOCE NAO PODE FINANCIAR ESSA CASA :(\033[m\n')
else:
	print('\n\033[1;33mCASA FINANCIADA :D\033[m\n')
	print('O valor da prestacao é de R$ {:.2f}'.format(prestacao))
