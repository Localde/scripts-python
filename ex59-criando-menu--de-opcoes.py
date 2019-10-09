a_valor = int(input('Digite um numero inteiro: '))
b_valor = int(input('Digite outro numero inteiro: '))
print('[1]SOMAR')
print('[2]MULTIPLICAR')
print('[3]MAIOR')
print('[4]NOVOS NUMEROS')
print('[5]SAIR DO PROGRAMA')
escolha = int(input())
while escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4 or escolha ==5:
    if escolha == 1:
        soma = a_valor + b_valor
        print(f'{a_valor} + {b_valor} = {soma}')
        escolha = int(input())
    elif escolha == 2:
        multiplicar = a_valor + b_valor
        print(f'{a_valor} x {b_valor} = {multiplicar}')
        escolha = int(input())
    elif escolha == 3:
        maior = 0
        if a_valor > b_valor:
            maior = a_valor
            print(f'Maior: {maior}')
            escolha = int(input())
        elif a_valor < b_valor:
            maior = b_valor
            print(f'Maior: {maior}')
            escolha = int(input())
        else:
            igual = a_valor == b_valor
            print(f'São iguais? {igual}')
            escolha = int(input())
    elif escolha == 4:
        a_valor = int(input('Digite um numero inteiro: '))
        b_valor = int(input('Digite outro numero inteiro: '))
        escolha = int(input())
    elif escolha == 5:
        break
    else:
        escolha = int(input('Essa opção não existe escolha outra:'))