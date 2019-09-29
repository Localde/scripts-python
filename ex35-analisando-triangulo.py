lado_a = float(input('Digite o valor de um lado do triângulo:'))
lado_b = float(input('Digite o valor de outro lado do triângulo: '))
lado_c = float(input('Digite o valor de outro lado do triângulo: '))

if lado_a >= lado_b and lado_a >= lado_c and lado_b + lado_c >= lado_a or lado_b >= lado_a and lado_b >= lado_c and lado_a + lado_c >= lado_b or lado_c >= lado_a and lado_c >= lado_b and lado_a + lado_b >= lado_c:
    print('É um triângulo.')
else:
    print('não é um triângulo.')
