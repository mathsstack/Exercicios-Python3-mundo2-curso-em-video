#Calcs the first 10 elements of an Arithimetic Progression

print('\n***PA CALC***\n')

first = int(input('Type the first element: '))
reason = int(input('Type the reason: '))
print('')

for c in range(0, 10):

	print(first + (c * reason))


