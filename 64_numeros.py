print('\n***NUMEROS***\n')

count = 0;
soma = 0
n = 0

while n != 999:

	n = int(input('Type a number: '))

	if n == 999:
		break
	count += 1
	soma += n

print(f'\nVoce digitou {count} números e a soma deles é {soma}')

