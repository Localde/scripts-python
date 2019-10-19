escolha = 999
cont = soma = 0
while escolha == 999:
    number = int(input('Digite um numero inteiro: '))
    if number == 999:
        break
    cont += 1
    soma += number
print(f'Quant. de numeros digitados: {cont}')
print(f'Soma dos numeros digitados: {soma}')