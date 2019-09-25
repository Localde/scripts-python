from random import sample

aluno1 = str(input('Digite um nome: '))
aluno2 = str(input('Digite um nome: '))
aluno3 = str(input('Digite um nome: '))
aluno4 = str(input('Digite um nome: '))

lista = [aluno1, aluno2, aluno3, aluno4]

print('O escolhido foi {}.'.format(sample(lista, 1)))
