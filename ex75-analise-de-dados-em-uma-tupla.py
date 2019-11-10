tupla = (
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: '))
)

lista = []

for cont in range(0, 4):
    if tupla[cont] % 2 == 0:
        lista.append(tupla[cont])
print(f'O 9 apareceu {tupla.count(9)} vezes.')
print(f'O primeiro 3 apareceu na {tupla.index(3) + 1} posição.')
print(f'Os numeros pares são {lista}.')