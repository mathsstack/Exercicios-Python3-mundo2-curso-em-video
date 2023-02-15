#Calculate the plus among every non par numbers between 1 and 50

print('\n***EXERCISE 48***\n')

interval = int(input('Escolha o limite maximo do intervalo: '))
soma = 0

for c in range(1, interval + 1):

	if (c % 2) != 0 and c % 3 == 0:
		soma += c


print(f'\nA soma entre os impares multiplos de 3 entre 1 e {interval} vale {soma}')

