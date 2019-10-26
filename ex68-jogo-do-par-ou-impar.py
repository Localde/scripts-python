from random import randint

cont = cont2 = 0

while True:
    print("""
    Faça a sua escolha:
    [1]Pedra;
    [2]Papel;
    [3]Tesoura.
    """)
    escolha = int(input())
    computador = randint(1, 3)
    if escolha == 1 and computador == 3 or escolha == 2 and computador == 1 or escolha == 3 and computador == 2:
        cont += 1
        print('Você GANHOU!!')
    elif escolha == 3 and computador == 1 or escolha == 1 and computador == 2 or escolha == 2 and computador == 3:
        print('Você PERDEU!!!')
        print(f'Total de Vitorias: {cont}')
        print(f'Total de Empates: {cont2}')
    else:
        cont2 += 1
        print('Você EMPATOU!!')