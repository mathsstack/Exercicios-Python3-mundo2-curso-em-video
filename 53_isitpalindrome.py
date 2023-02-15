#Verifica se uma frase é palindroma

print('\n***É PALÍNDROMA??***\n')

frase = input('Digite sua frase: ')

splitado = frase.split()
junto = ''

for c in range(0, len(splitado)):
	junto += splitado[c]

normalize = junto.upper()
palindrome = False

for c in range(0, len(normalize)): 

	if normalize[c] == normalize[len(normalize) - 1 - c]:

		palindrome = True
	else:
		palindrome = False
		break

if palindrome == True:
	print(f'\n"{frase}" é palíndroma')
else:
	print(f'\n{frase} não é palindroma')
