cont = soma = 0
while True:
    number = int(input('Digite um numero: '))
    if number != 999:
        cont += 1
        soma += number
    else:
        print(f'Quantidade: {cont}')
        print(f'Soma: {soma}')
        break