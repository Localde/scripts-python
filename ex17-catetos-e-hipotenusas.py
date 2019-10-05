from math import sqrt

cateto_oposto = float(input('Digite o cateto aposto do triângulo: '))
cateto_adjacente = float(input('Digite o cateto adjacente do triângulo: '))
hipostenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
print(f'A hipotenusa é igual a {hipostenusa}')