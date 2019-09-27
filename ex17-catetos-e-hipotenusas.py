from math import hypot
cateto_oposto = float(input('Digite seu cateto oposto: '))
cateto_adjacente = float(input('Digite seu cateto adjacente: '))

print(f'A sua hipotenusa é igual a {hypot(cateto_oposto, cateto_adjacente)}')