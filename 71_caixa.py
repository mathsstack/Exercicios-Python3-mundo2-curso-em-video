print('\n***BEM VINDO AO BANCO GBANK***\n')

terminar = False

while terminar == False:

	notascinquenta = 0
	notasvinte = 0
	notasdez = 0
	notasum = 0

	valor = int(input('Digite o valor para saque: '))

	notascinquenta = valor // 50
	notasvinte = (valor % 50) // 20
	notasdez = ((valor % 50) % 20) // 10
	notasum = (((valor % 50) % 20) % 10)

	print(f'''\nResultado:

{notascinquenta} notas de R$ 50.00.
{notasvinte} notas de R$ 20.00.
{notasdez} notas de R$ 10.00
{notasum} notas de R$ 1.00''')

	while True:
		continuar = input('\nSacar novamente [S/N]? ').strip().upper()
		if continuar == 'N':
			terminar = True
		if continuar == 'S' or continuar == 'N':
			break
