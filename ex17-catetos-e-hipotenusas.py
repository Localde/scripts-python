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
co = float(input('\033[1;31mComprimento do cateto oposto: '))
ca = float(input('\033{1;34mComprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('\033[1;33mA hipotenusa vai medir \033[1;30m{:.2f}'.format(hi))
