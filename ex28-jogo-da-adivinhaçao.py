#from random import randint

#numero = int(input('Digite um numero de 0 a 5: '))
#aleatorio = randint(0, 5)

#if numero == aleatorio:
    #print('Você Ganhou!')
#else:
    #print('Você perdeu!')
#print('FIM DO PROGRAMA!!!')
from random import randint
from time import sleep

computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
