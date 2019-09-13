from math import sqrt

oposto = int(input('Digite o valor do cateto oposto: '))
adjacente = int(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é de {}'.format(sqrt((oposto * oposto) + (adjacente * adjacente))))
