#Verifica as propriedades de um triangulo

print('\n***WHICH TRIANGLE***\n')

l1 = float(input('Digite a medida do lado 1: '))
l2 = float(input('Digite a medida do lado 2: '))
l3 = float(input('Digite a medida do lado 3: '))

if l1 == l2 == l3:

	print('\nO triângulo é equilátero\n')

elif l1 != l2 != l3:

	print('\nO triangulo é escaleno\n')

else:

	print('\nO triangulo é isosceles\n')
