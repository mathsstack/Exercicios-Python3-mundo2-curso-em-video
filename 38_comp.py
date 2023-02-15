#Avalia se dois inteiros sao iguais ou nao

print('\n***MAIOR E MENOR***\n')

n1 =int(input('Digite um número: '))
n2 =int(input('Digite outro número: '))

if n1 == n2:
	print('\nOs dois números sao iguais')
elif n1 > n2:
	print('\nO número {} é maior'.format(n1))
else:
	print('\nO número {} é maior'.format(n2))

