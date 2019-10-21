cont = soma = 0
while True:
    number = int(input('Digite um numero inteiro: '))
    if number == 999:
        break
    cont += 1
    soma += number
print(f'Quantidade de numeros digitados: {cont}')
print(f'Soma entre esses numeros: {soma}')