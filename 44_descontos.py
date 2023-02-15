#Calcula descontos de acordo com a forma de pagamento

print('\n***CALCULADORA DE DESCONTOS 2.0***\n')

valor = float(input('Digite o valor do produto: R$ '))

opcao = int(input('''\nEscolha a forma de pagamento: 

(1) À vista em dinheiro
(2) À vista no cartão
(3) 2x no cartão
(4) 3x no cartão

Digite: '''))

if opcao == 1:

	valor = valor * 0.9

elif opcao == 2:

	valor = valor * 0.95

elif opcao == 3:

	valor = valor / 2

elif opcao == 4:

	valor = (valor * 1.2) / 3

else:
	print('\nDigite uma opcao válida\n')


if opcao == 3 or opcao == 4:

	print('O valor a ser pago fica {}x de R% {}'.format(opcao - 1, valor))
else:
	print('O valor a ser pago fica R$ {}'.format(valor))
