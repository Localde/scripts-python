from random import sample

nome_1 = str(input('Digite um nome: '))
nome_2 = str(input('Digite um nome: '))
nome_3 = str(input('Digite um nome: '))
nome_4 = str(input('Digite um nome: '))

lista = [nome_1, nome_2, nome_3, nome_4]

print(sample(lista, 4))
