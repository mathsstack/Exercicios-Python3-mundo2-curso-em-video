count = 0
soma = 0

while True:
	c = int(input('Type a number: '))

	if c == 999:
		break
	soma += c
	count += 1

print(f'\nA soma dos {count} numeros foi {soma}')

