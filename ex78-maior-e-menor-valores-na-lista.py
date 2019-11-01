lista = []

for pos in range(0, 4):
    lista.append(int(input('Digite um numero: ')))
    if pos == 0:
        maior = lista[pos]
        menor = lista[pos]
    elif lista[pos] > maior:
        maior = lista[pos]
        posição = pos + 1
    elif lista[pos] < menor:
        menor = lista[pos]
        posição2 = pos + 1
print(f'Maior: {maior} e sua posição é {posição}')
print(f'Menor: {menor} e sua posição é {posição2}')