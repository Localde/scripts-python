matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_de_pares = 0
soma_3_coluna = 0
ver = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_de_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_3_coluna += matriz[linha][coluna]
        if ver == 0:
            maior = matriz[linha][coluna]
            ver += 1
        elif matriz[1][coluna] > maior:
            maior = matriz[linha][coluna]
print(f'A soma de todos os valores pares digitados: {soma_de_pares}')
print(f'A soma dos valores da terceira coluna: {soma_3_coluna}')
print(f'O maior valor da segunda linha: {maior}')

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()