tupla = 'carro', 2, 'moto', 3, 'bicicleta', 5
pos = 0
for item in tupla:
    if pos % 2 == 0 or pos == 0:
        print(f'{item}{"." * 30} ', end='')
    else:
        print(f'R${item:.2f}')
    pos += 1
