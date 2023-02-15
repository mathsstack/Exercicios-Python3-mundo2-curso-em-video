#Converte um decimal para outras bases:

print('\n***CONVERSOR DE BASES***\n')

num = int(input('Digite o número a ser convertido: '))

print('''\nEscolha a base para a qual o numero sera convertido:
(1) Binario
(2) Octal
(3) Hexadecimal''')

base = int(input('\n'));

binary = bin(num)
octa = oct(num)
hexa = hex(num)

if base == 1:
	print('O valor em binário é {}'.format(binary[2:]))
elif base == 2:
	print('O valor em octal é {}'.format(octa[2:]))
elif base == 3:
	print('O valor em hexadecimal é {}'.format(hexa[2:]))
else:
	print('\033[1;31mDIGITE UMA OPCAO VÁLIDA\033[m')
