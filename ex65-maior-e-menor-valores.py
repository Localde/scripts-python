soma = cont = maior = menor = 0
while True:
    number = int(input('Digite um numero inteiro: '))
    cont += 1
    soma += number
    media = soma / cont
    if cont == 1:
        maior = number
        menor = number
    elif number > maior:
        maior = number
    elif number < menor:
        menor = number
    escolha = str(input('Deseja continuar [s] [n]? '))
    if escolha == 'n':
        break
print(f'A média é igual a: {media}')
print(f'O maior é {maior}')
print(f'O menor é {menor}')