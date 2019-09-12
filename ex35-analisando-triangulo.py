a = int(input('Digite o tamanho do lado A do triangulo: '))
b = int(input('Digite o tamanho do lado B do triangulo: '))
c = int(input('Digite o tamanho do lado C do triangulo: '))

print('É um triângulo.' if a >= b and a >= c and b + c >= a or b >= a and b >= c and a + c >= b or c >= a and c >= b and a + b >= c else 'Não é Triângulo.')
