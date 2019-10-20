from random import randint
cont = 0
while True:
    print('Escolha um numero de 0 à 5.')
    escolha = int(input())
    escolha2 = str(input('Você quer ser par ou impar? [p][i]'))
    computador = randint(0, 5)

    if escolha2 == 'p' and (escolha + computador) % 2 == 0:
        print('Você ganhou!')
        print(f'Maquina: {computador}')
        cont += 1
    elif escolha2 == 'i' and (escolha + computador) % 2 != 0:
        print('Você ganhou!')
        print(f'Maquina: {computador}')
        cont += 1
    else:
        break

print(f'Total de vitórias consecutivas: {cont}')