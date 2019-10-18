opção = str('s')
soma = 0
media = 0
maior = menor = 0
while opção == 's':
    number = int(input('Digite um numero inteiro: '))
    opção = str(input('Deseja continuar? [s] or [n] ')).lower()
    if opção != 'n' and opção != 's':
        print('Esta opção é invalida.')
        break
    soma += number
    media += 1

    if media == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number
if soma == 0 or media == 0:
    print('Não tem como realizar a média.')
else:
    print(f'Média: {soma/media}')
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')