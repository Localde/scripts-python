valores = (
    int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite outro numero: '))
)

if 9 in valores:
    print(f'Numero de vezes que apareceu o 9: {valores.count(9)} vezes.')
else:
    print('Não apareceu o numero 9.')
if 3 in valores:
    print(f'O numero 3 aparece pela primeira vez na {valores.index(3)} posição.')
else:
    print('Não apareceu o numero 3.')
print('Os valores pares são: ', end=' ')
for valor in valores:
    if valor % 2 == 0:
        print(f'{valor} ', end='')
    else:
        continue
