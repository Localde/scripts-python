a = float(input('Escreva o tamanho do lado A: '))
b = float(input('Escreva o tamanho do lado B: '))
c = float(input('Escreva o tamanho do lado C: '))

if a >= b and a >= c and b + c >= a or b >= a and b >= c and a + c >= b or c >= a and c >= b and a + b >= c:
    print('É um triângulo.')
else:
    print('Não é um triângulo.')
