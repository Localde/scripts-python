#import random
#nome1 = str(input('Digite um nome: '))
#nome2 = str(input('Digite outro nome: '))
#nome3 = str(input('Digite outro nome: '))
#nome4 = str(input('Digite outro nome: '))
#lista = [nome1, nome2, nome3, nome4]
#sorteado = random.choice(lista)

#print('O escolhido foi {}.'.format(sorteado))
from random import choice
nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite outro nome: '))
nome3 = str(input('Digite outro nome: '))
nome4 = str(input('Digite outro nome: '))
lista = [nome1, nome2, nome3, nome4]
sorteado = choice(lista)

print('O escolhido foi {}.'.format(sorteado))
