soma = 0
for alunos in range(1, 3):
    print('Digite sua nota: ')
    nota = float(input())
    soma += nota
    media = soma / alunos
print(f'A média entre os alunos é de: {media}')