from time import sleep

print('\n***CALCULADORA***\n')

sair = 0

while sair == 0:
	maior = 0
	menor = 0
	resultado = 0
	n1 = float(input('Digite um valor: '))
	n2 = float(input('Digite outro valor: '))

	opcao = int(input('''Agora escolha: 

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Digite: '''))

	if opcao < 3 and opcao > 0:

		if opcao == 1:

			resultado = n1 + n2
		elif opcao == 2:
			resultado = n1 * n2

		print(f'O resultado é {resultado}')

	elif opcao == 3:
		if n1 > n2:
			maior = n1
			menor = n2
		elif n1 < n2:
			maior = n2
			menor = n1
		else:
			print('Os números são iguais!')

		print(f'{maior} é maior do que {menor}')

	elif opcao == 4:
		print('Reiniciando....')
		sleep(5)
	elif opcao == 5:
		print('Saindo...')
		sleep(2)
		sair = 1
	else:
		print('ENTRADA INVÁLIDA')

