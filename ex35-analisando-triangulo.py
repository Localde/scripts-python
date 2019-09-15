a = int(input('Digite o comprimento da reta A: '))
b = int(input('Digite o comprimento da reta B: '))
c = int(input('Digite o comprimento da reta C: '))

print('É um triângulo.' if a >= b and a >= c and b + c >= a or b >= a and b >= c and a + c >= b or c >= a and c >= b and a + b >= c else 'Não é um triângulo.')
