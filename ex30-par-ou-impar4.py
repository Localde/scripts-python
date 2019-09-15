numero = int(input('Digite um numero: '))

if numero == 0:
    print('O numero é neutro.')
else:
    if numero % 2 == 0:
        print('O numero é par.')
    else:
        print('O numero é impar.')