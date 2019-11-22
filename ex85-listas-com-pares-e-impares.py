lista = []

for cont in range(0, 7):
    lista.append(int(input('Digite um valor: ')))
print('Par: ', end='')
for cont in range(0, len(lista)):
    if lista[cont] % 2 == 0:
        print(f'{lista[cont]}', end=' ')
print('\n')
print('Impar: ', end='')
for cont in range(0, len(lista)):
    if lista[cont] % 2 != 0:
        print(f'{lista[cont]}', end=' ')

