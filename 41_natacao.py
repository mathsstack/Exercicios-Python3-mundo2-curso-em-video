from datetime import datetime

today = datetime.now().date().year

#Verifica a classificacao de um atleta de natacao

print('\n***CATEGORIAS DE NATACAO***\n')

ano = int(input('Digite o seu ano de nascimento: '))

idade = today - ano

if idade <=9:

	print('\nSua categoria é Mirim\n')

elif 9 < idade <= 14:

	print('\nSua categoria é infantil\n')

elif 14 < idade <19:

	prinr('\nSua categoria é júnior\n')

elif 19 <= idade <=20:

	print('\nSua categoria é Sênior\n')
else:

	print('\nSua categoria é Master\n')

