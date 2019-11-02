nún = (
    int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite o ultimo numero: '))
)
print(f'Você digitou os valores {nún}')
print(f'O valor 9 apareceu {nún.count(9)} vezes.')
if 3 in nún:
    print(f'O valor 3 apareceu na {nún.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in nún:
    if n % 2 == 0:
        print(n, end=' ')