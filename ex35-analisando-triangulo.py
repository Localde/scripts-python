a = int(input('Digite o valor do primeiro lado:'))
b = int(input('Digite o valor do segundo lado:'))
c = int(input('Digite o valor do terceiro lado:'))

print('É um triangulo.' if a >= b and a >= c and b + c >= a or b >= a and b >= c and a + c >= b or c >= a and c >= b and a + b >= c else 'Não é um triângulo')