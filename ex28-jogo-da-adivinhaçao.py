from random import randint
tentativa = int(input('Digite um numero de 0 a 5: '))
pensando = randint(0, 6)
print('Acertou Miseravel!!!' if tentativa == pensando else 'Errou! Tente Novamente.')
