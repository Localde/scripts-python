numero = int(input('Digite um numero de 0 a 9999: '))

unidade = numero // 1 % 10

print('Unidade: {}'.format(unidade))

dezena = numero // 10 % 10

print('Dezena: {}'.format(dezena))

centena = numero // 100 % 10

print('Centena: {}'.format(centena))

milhar = numero // 1000 % 10

print('Milhar: {}'.format(milhar))
