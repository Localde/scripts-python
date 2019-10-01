number = int(input('Digite um numero inteiro: '))
soma = 0
#O NUMERO SÓ PODE SER DIVISIVEL POR 1 OU POR ELE MESMO.

if number % 2 != 0:
    for cont in range(2, number + 1):
        if number % cont == 0:
            soma = soma + 1

    if soma == 1:
        print('é primo')

else:
    print('Não é primo')