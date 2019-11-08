from random import randint
a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)
tupla = (a, b, c, d, e)
verifica = 0
for variavel in tupla:
    if verifica == 0:
        maior = variavel
        menor = variavel
        verifica += 1
    elif variavel > maior:
        maior = variavel
    elif variavel < menor:
        menor = variavel
print(tupla)
print(f'Maior = {maior}')
print(f'Menor = {menor}')