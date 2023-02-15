#verifica se um aluno foi aprovado

print('\n***PASSOU DE ANO?***\n')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
	print('\n\033[1;31mREPROVADO :(\033[m\n')
elif 5 < media < 7:
	print('\n\033[1;33mRECUPERAÇÃO :/\033[m\n')
else:
	print('\n\033[1;32mAPROVADO :D\033[m\n')
