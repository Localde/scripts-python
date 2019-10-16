cont = 0
soma = 0
number = 0
while number != 999:
    number = int(input('Digite um numero: '))
    if number == 999:
        break
    soma += number
    cont += 1
print(f'Quantidade de numeros digitados: {cont}')
print(f'Soma dos numeros digitados: {soma}')