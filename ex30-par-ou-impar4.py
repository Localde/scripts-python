numero = int(input('Digite um numero inteiro qualquer:'))
if numero == 0:
    print('É neutro')
if numero % 2 == 0 and numero != 0:
    print('É par.')
if numero % 2 != 0 and numero != 0:
    print('É impar.')
