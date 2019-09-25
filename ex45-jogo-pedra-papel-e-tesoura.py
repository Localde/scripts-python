from random import randint

print('Digite 1 para Pedra.')
print('Digite 2 para papel.')
print('Digite 3 para tesoura.')

escolha = int(input())

maquina = randint(1, 3)

if maquina == 1 and escolha == 3 or maquina == 2 and escolha == 3 or maquina == 3 and escolha == 1:
    print('Você ganhou!')
elif escolha == 1 and maquina == 3 or escolha == 2 and maquina == 3 or escolha == 3 and maquina == 1:
    print('Você perdeu!')
else:
    print('Empatou!')
