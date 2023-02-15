#Ler informacoes e retornar valores:

print('\n***ANALYTICS***\n')

agesomatory = 0
oldage = 0
less20women = 0
iold = 0


#qtde = int(input('Quantas pessoas quer analisar? '))
names = ['', '', '', '', ]

for c in range(0, 4):

	name = str(input('\nDigite seu nome: '))
	age = int(input('Digite sua idade: '))
	sexo = int(input('Escolha o sexo: (1) Homem (2) Mulher: '))

	names[c] = name
	agesomatory += age

	if sexo == 1 and age > oldage:
		iold = c
		oldage = age
	if sexo == 2 and age < 20:
		less20women += 1

	print(f'\n***PESSOA {c + 1} ANALISADA!')

media = agesomatory / 4

print(f'''
\n
***RESULTADO***

Médias das idades: {media}
Homem mais velho: {names[iold]}
Mulheres com menos de 20 anos: {less20women}
\n''')
