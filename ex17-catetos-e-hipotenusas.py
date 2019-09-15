from math import sqrt

a = int(input('Digite o cateto Oposto: '))
b = int(input('Digite o cateto adjacente: '))

print('A hipotenusa é igual a {}.'.format(sqrt((a * a) + (b * b))))
