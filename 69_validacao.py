maior = 0
men = 0
mvinte = 0

while True:

	age = int(input('Idade: '))

	while True:
		sex = input('Sexo [M/F]: ').strip().upper()

		if sex == 'M' or sex == 'F':
			break

	if age > 18:
		maior+=1
	if sex == 'M':
		men += 1
	if sex == 'F' and age < 20:
		mvinte += 1

	choice = input('Deseja digitar mais dados [S/N]? ').strip().upper()

	if choice == 'N':
		break

print(f'''\nANÁLISE:

{maior} pessoas sao maiores de idade
{men} homens foram cadastrados
{mvinte} mulheres tem menos de 20 anos''')
