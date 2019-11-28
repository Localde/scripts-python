lista_de_produtos = ('Lapis', 5, 'Caneta', 2, 'Borracha', 1)
cont = 0
print('-' * 45)
for produto in lista_de_produtos:
    if cont % 2 == 0:
        print(f'{produto}', '-' * 25, end=' ')
    else:
        print(f'R${produto:.2f}')
    cont += 1
print('-' * 45)