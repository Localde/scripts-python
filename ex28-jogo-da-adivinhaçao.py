from random import randint

aleatorio = randint(1, 5)
chute = int(input('Adivinhe o numero que estou pensando: '))
print('Você acertou!' if chute == aleatorio else 'Você errou!')
