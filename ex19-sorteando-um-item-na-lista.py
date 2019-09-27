from random import sample

aluno_1 = str(input('Digite o nome de um aluno: '))
aluno_2 = str(input('Digite o nome de outro aluno: '))
aluno_3 = str(input('Digite o nome de outro aluno: '))
aluno_4 = str(input('Digite o nome de outro aluno: '))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

print(f'O aluno escolhido foi {sample(lista, 1)}')
