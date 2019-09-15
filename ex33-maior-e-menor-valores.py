a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))

if a > b and a > c:
    print('Maior: {} \nMenor: {}'.format(a, c) if b > c else 'Maior: {} \n Menor: {}'.format(a, b))
elif b > a and b > c:
    print('Maior: {} \n Menor: {}'.format(b, c) if a > c else 'Maior: {} \n Menor: {}'.format(b, a))
else:
    print('Maior: {} \n Menor: {}'.format(c, b) if a > b else 'Maior: {} \n Menor: {}'.format(c, a))
