#oposto = float(input('Digite o Cateto Oposto: '))
#adjacente = float(input('Digite o Cateto Adjacente: '))
#hipotenusa = (oposto ** 2 + adjacente ** 2) ** 0.5
#print('O comprimento da hipotenusa é de {:.2f}.'.format(hipotenusa))
#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = math.hypot(co, ca)

#print('A hipotenusa vai medir {:.2f}'.format(hi))
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
