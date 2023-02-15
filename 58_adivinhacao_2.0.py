from random import randint

#A máquina chuta um número e o jogador tenta adivinhar

print('\n\033[36m***JOGO DE ADIVINHACAO***\n')

secrtnum = randint(0, 10)
acertou = 0
chutes = 0

while acertou == 0:

	chute = int(input('Qual é o seu chute? '))
	chutes += 1

	if chute == secrtnum:
		print('\nPARABENS! Voce acertou! \n')
		print(f'\nVoce precisou de {chutes} chutes pra acertar!\n')
		acertou = 1
	else:
		print('\nF,voce errou!\n')

print('***FIM DE JOGO***\033[m\n')
