print('\n***NUMBERS 2.0***\n')

quer = 'S'
soma = 0
maior = 0
menor = 0
vezes = 10
c = 0

while quer == 'S':

	vezes = int(input('Quantos números quer digitar? '))

	while c < vezes:

		n = int(input('Type a number: '))
		soma += n

		if c == 0:
			maior = n
			menor = n

		elif n > maior:
			maior = n
		elif n < menor:
			menor = n
		c += 1

	print(f'\nA media dos números é {soma/c}')
	print(f'O maior número foi {maior} e o menor foi {menor}')
	quer = input('\nDeseja digitar mais números? ')
