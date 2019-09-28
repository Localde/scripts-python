from random import randint

numero = int(input('Digite um numero de 0 a 5: '))

computador = randint(0, 5)

if numero == computador:
    print('Voce venceu.')
else:
    print(f'Voce perdeu pois o computador escolheu o {computador}')
