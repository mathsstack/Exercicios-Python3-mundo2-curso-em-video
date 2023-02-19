from random import randint

print('*'*18)
print('***PAR OU ÍMPAR***')
print('*'*18)

vitorias = 0

while True:

	jmaquina = randint(0, 10)

	jplayer = int(input('Qual a sua jogada? '))

	choice = input('Par ou ímpar [P/I]? >>> ').strip().upper()

	if choice == 'P' and (jmaquina + jplayer) % 2 != 0:
		break
	elif choice == 'I' and (jmaquina + jplayer) % 2 == 0:
		break

	print('\nVOCE GANHOU!')
	vitorias+=1

print(f'\nVOCE PERDEU! voce fez {vitorias} vitorias consecutivas!')
