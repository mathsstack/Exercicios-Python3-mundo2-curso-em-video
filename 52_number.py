#Verifica se um número é primo:

print('\n***NÚMEROS PRIMOS***\n')

num = int(input('Digite um número: '))

for c in range(2, num):

	if (num // c) < c:
		print(f'\nO número {num} é primo!')
		break

	if num % c == 0:
		print(f'\nO número {num} nao é primo!')
		break
