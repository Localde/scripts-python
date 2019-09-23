from random import sample

nome_1 = str(input('Digite um nome: '))
nome_2 = str(input('Digite outro nome: '))
nome_3 = str(input('Digite outro nome: '))
nome_4 = str(input('Digite outro nome: '))

names = [nome_1, nome_2, nome_3, nome_4]

print('O escolhido foi {}'.format(sample(names, 1)))
