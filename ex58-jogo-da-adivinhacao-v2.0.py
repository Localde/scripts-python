from random import randint

print('Adivinhe o numero que estou pensando: ')
escolha = int(input())
maquina = randint(0, 10)

while escolha != maquina:
    escolha = int(input('Você não acertou. Tente novamente: '))