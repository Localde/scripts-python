primeiro_termo = int(input('Qual é o primeiro termo da P.A.? '))
razao = int(input('Qual é a razão? '))

for cont in range(primeiro_termo, primeiro_termo + 10):
    primeiro_termo += razao
    print(primeiro_termo, end=' ')