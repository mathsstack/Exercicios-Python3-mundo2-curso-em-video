#Among six numbers it will coung only the par numbers

print('\n***COUNT***\n')

soma = 0;

for c in range(0, 6): 

	num = int(input('Type a number: '))

	if num % 2 == 0:
		soma += num

print(f'\nThe count among the par numbers equals {soma}')

