#O computador joga jokenpo com voce

import random

print('''\n

       __    ______    __  ___  _______ .__   __. .______     ______   
      |  |  /  __  \  |  |/  / |   ____||  \ |  | |   _  \   /  __  \  
      |  | |  |  |  | |  '  /  |  |__   |   \|  | |  |_)  | |  |  |  | 
.--.  |  | |  |  |  | |    <   |   __|  |  . `  | |   ___/  |  |  |  | 
|  `--'  | |  `--'  | |  .  \  |  |____ |  |\   | |  |      |  `--'  | 
 \______/   \______/  |__|\__\ |_______||__| \__| | _|       \______/  


''')

artes = [

 '''
    ____
  _/  _ \\
 / _ - _ \\
 \\_______/''' ,

'''
   _____
  O_____O
  /     /
 /____ /
O_____O

''',

 '''
    _    _
   (_)  / )
     | (_/
    _+/
   //|\\
  // ||
 (/  |/

''',
'''
   _______      ___      .__   __.  __    __    ______    __    __
  /  _____|    /   \     |  \ |  | |  |  |  |  /  __  \  |  |  |  |
 |  |  __     /  ^  \    |   \|  | |  |__|  | |  |  |  | |  |  |  |
 |  | |_ |   /  /_\  \   |  . `  | |   __   | |  |  |  | |  |  |  |
 |  |__| |  /  _____  \  |  |\   | |  |  |  | |  `--'  | |  `--'  |
  \______| /__/     \__\ |__| \__| |__|  |__|  \______/   \______/

''',

'''
 _______ .___  ___. .______        ___      .___________.  ______    __    __
|   ____||   \/   | |   _  \      /   \     |           | /  __  \  |  |  |  |
|  |__   |  \  /  | |  |_)  |    /  ^  \    `---|  |----`|  |  |  | |  |  |  |
|   __|  |  |\/|  | |   ___/    /  /_\  \       |  |     |  |  |  | |  |  |  |
|  |____ |  |  |  | |  |       /  _____  \      |  |     |  `--'  | |  `--'  |
|_______||__|  |__| | _|      /__/     \__\     |__|      \______/   \______/

''',

'''
.______    _______ .______       _______   _______  __    __
|   _  \  |   ____||   _  \     |       \ |   ____||  |  |  |
|  |_)  | |  |__   |  |_)  |    |  .--.  ||  |__   |  |  |  |
|   ___/  |   __|  |      /     |  |  |  ||   __|  |  |  |  |
|  |      |  |____ |  |\  \----.|  '--'  ||  |____ |  `--'  |
| _|      |_______|| _| `._____||_______/ |_______| \______/

'''

]

vplayer = 0
vpc = 0
sair = 1

while sair == 1:

	pcschoice = random.randint(1,3)

	jogada = int(input('''\nEscolha a sua jogada: 


(1) Pedra
(2) Papel
(3) Tesora

Jogue: '''))

	if jogada < 1 or jogada > 3:

		print('\nJOGADA INVÁLIDA\n')
		continue
	else:

		print('''

 	Você:

  	{}

	Máquina:

  	{}

	'''.format(artes[jogada-1], artes[pcschoice-1]))

	if pcschoice == (jogada - 1):

		vplayer = vplayer + 1

	elif pcschoice == (jogada - 2):

		vpc = vpc + 1

	elif jogada == (pcschoice - 2):

		vplayer = vplayer + 1

	elif jogada == (pcschoice -1):

		vpc = vpc + 1

	print('''\nPLACAR: 

JOGADOR: {}
MÁQUINA: {}\n'''.format(vplayer, vpc))

	erro = 1
	while erro == 1:

		playagain = int(input('\nJogar Novamente? (1)Sim (2)Não: '))

		if playagain <1 or playagain > 2:
			print('\n\033[31mCOMANDO INVÁLIDO\033[m\n')
		else:
			sair = playagain
			erro = 0



else:
	if vplayer >  vpc:
		print('\033[32m{}\033[m'.format(artes[3]))
	elif vplayer == vpc:
		print('\033[33m{}\033[m'.format(artes[4]))
	else:
		print('\033[31m{}\033[m'.format(artes[5]))

	print('\nFIM DE JOGO\n')
