#Calcula imc

print('\n***CALCULADORA DE IMC***\n')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

print('\nSeu IMC é igual a {:.1f}\n'.format(imc))

if imc < 18.5:

	print('Voce está abaixo do peso ideal')

elif 18.5 <= imc < 25:

	print('Voce está no peso ideal')

elif 25 <= imc <30:

	print('Voce esta na faixa de sobrepeso')

elif 30 <= imc <= 40:

	print('Voce esta com obesidade')

else:

	print('Voce está com obesidade mórbida')

