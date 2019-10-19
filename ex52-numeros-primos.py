number = int(input('Digite um número: '))
resultado = 0

for cont in range(2, number + 1):
    if number % cont == 0:
        resultado += 1
if resultado == 1:
    print('É um primo')
else:
    print('Não é um numero primo.')
