lista_de_produtos = 'Caderno', 2, 'Caneta', 1, 'Lapis', 1
cont = 0
for item in lista_de_produtos:
    if cont % 2 == 0:
        print(f'{item}', '-' * 30, end='')
    else:
        print(f'R${item:.2f}')
    cont += 1