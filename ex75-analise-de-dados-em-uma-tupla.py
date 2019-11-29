valores = (
    int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite outro valor: '))
)

print(f'Quantidade de numero 9 digitado: {valores.count(9)}')
print(f'Posição do 1º numero 3 digitado: {valores.index(3) + 1}')
print('Os numeros pares são: ', end='')

for a in range(0, 4):
    if valores[a] % 2 == 0:
        print(valores[a], end=' ')