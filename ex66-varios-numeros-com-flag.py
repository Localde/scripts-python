number = cont = soma = 0
while number != 999:
    number = int(input('Digite um numero inteiro: '))
    if number != 999:
        cont += 1
        soma += number
print(f'Quantidade: {cont}')
print(f'Soma: {soma}')