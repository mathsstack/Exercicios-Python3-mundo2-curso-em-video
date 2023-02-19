print('\n***SUPERMARKET***\n')

continuar = 'S'

total = 0
mmil = 0
pmbarato = 0
mbarato = ''

while continuar == 'S':

	nome = input('Nome do produto: ')
	preco = float(input('Preço: R$ '))

	if total == 0:
		pmbarato = preco

	if preco > 1000:
		mmil+=1

	if preco < pmbarato:
		mbarato = nome

	total+=preco

	while True:
		continuar = input('Deseja continuar [S/N]? ').strip().upper()
		if continuar == 'S' or continuar == 'N':
			break

print(f'''\nANALISE:

O total da compra foi R$ {total}
O produto mais barato foi {mbarato}
{mmil} produtos custam mais de R$ 1000.00''')
