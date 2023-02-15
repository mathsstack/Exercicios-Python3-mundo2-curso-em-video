import datetime

currentdate = datetime.datetime.now()
data = currentdate.date()

#Verifica se um jovem deve fazer o alistamento militar

print('\n***ALISTAMENTO MILITAR***\n')

ano = int(input('Digite o ano do seu nascimento: '))

idade = data.year - ano

if idade < 18:
	print('\nAinda faltam {} anos pra voce se alistar\n'.format(18 - idade))
elif idade == 18:
	print('\nVoce deve se alistar esse ano\n')
else:
	print('\nJa passou {} anos do prazo pra se alistar\n'.format(idade - 18))

