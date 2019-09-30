number = int(input('Digite um numero: '))

for cont in range(0, number):
    div = number % cont
        if div != 0:
            print('é primo')
        else:
            print('Não é primo.')