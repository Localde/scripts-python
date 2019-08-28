#import random

#nome1 = str(input('Digite um nome: '))
#nome2 = str(input('Digite outro nome: '))
#nome3 = str(input('Digite outro nome: '))
#nome4 = str(input('Digite outro nome: '))

#lista = [nome1, nome2, nome3, nome4]

#random.shuffle(lista)

#print('{}'.format(lista))
from random import shuffle

nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite outro nome: '))
nome3 = str(input('Digite outro nome: '))
nome4 = str(input('Digite outro nome: '))

lista = [nome1, nome2, nome3, nome4]

shuffle(lista)

print('{}'.format(lista))
