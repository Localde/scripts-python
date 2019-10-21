from random import randint
cont = 1
while True:
    escolha = int(input('Digite um numero de 0 a 10: '))
    maquina = randint(0, 10)
    if escolha != maquina:
        cont += 1
        print(f'Maquina pensou: {maquina}')
    else:
        break
print(f'Foram necessarios {cont} tentativas para acertar.')