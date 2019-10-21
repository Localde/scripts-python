from random import randint
escolha = int(input('Digite um numero de 0 a 5: '))
maquina = randint(0, 5)
if escolha == maquina:
    print(f'Acertou Miseravel!')
else:
    print(f'Errooooou!')