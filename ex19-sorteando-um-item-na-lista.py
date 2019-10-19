from random import sample

a_aluno = str(input('Digite o nome do aluno: '))
b_aluno = str(input('Digite o nome de outro aluno: '))
c_aluno = str(input('Digite o nome de outro aluno: '))
d_aluno = str(input('Digite o nome de outro aluno: '))

lista = [a_aluno, b_aluno, c_aluno, d_aluno]

escolhido = sample(lista, 1)

print(escolhido)