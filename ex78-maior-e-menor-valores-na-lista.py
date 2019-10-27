listanum = []
maior = 0
menor = 0
for cont in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {cont}: ')))

    if cont == 0:
        maior = menor = listanum[cont]
    else:
        if listanum[cont] > maior:
            maior = listanum[cont]
        if listanum[cont] < menor:
            menor = listanum[cont]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior}', end='')
for i, v, in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor velor digitado foi {menor}', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
print()