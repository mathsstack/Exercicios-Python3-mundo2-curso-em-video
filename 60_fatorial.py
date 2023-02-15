print('\n***FATORIAL***\n')

entrada = int(input('Digite um número: '))
fatorial = n = entrada
n -= 1

while n > 1:
	fatorial = fatorial * n
	n -= 1

print(f'\nO fatorial de {entrada} vale {fatorial}')
