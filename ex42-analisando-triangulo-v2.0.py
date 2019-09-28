a__lado = int(input('Digite o lado A: '))
b_lado = int(input('Digite o lado B: '))
c_lado = int(input('Digite o lado C: '))

if a__lado >= b_lado and a__lado >= c_lado and b_lado + c_lado >= a__lado or b_lado >= a__lado and b_lado >= c_lado and a__lado + c_lado >= b_lado or c_lado >= a__lado and c_lado >= b_lado and a__lado + b_lado >= c_lado:
    if a__lado == b_lado and b_lado == c_lado:
        print('É um triângulo equilatero.')
    elif a__lado == b_lado or b_lado == c_lado or c_lado == a__lado:
        print('É um triângulo Isósceles.')
    else:
        print('É um triângulo escaleno.')
else:
    print('Não é um triângulo.')