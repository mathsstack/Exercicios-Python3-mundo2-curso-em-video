#Mostra o maior e o maior peso entre 6 pessoas:

print('\n***FAT OR THINNY??***\n')

maior = 0
menor = 0

for c in range(1, 6):

	peso = int(input(f'Digite o peso da {c}° pessoa: '))

	if peso > maior:
		maior = peso
	elif peso < menor:
		menor = peso

	if c == 2:
		if peso < maior:
			menor = peso
		elif peso >= maior:
			menor = maior
			maior = peso
if maior == menor:
	print('\nOs dois pesos sao iguais')
else:
	print(f'\nO maior peso é {maior} e o menor peso é {menor}')
