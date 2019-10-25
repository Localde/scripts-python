produtos_preços = ('carro', 20000,
                   'casa', 40000,
                   'televisão', 2000)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos_preços)):
    if pos % 2 == 0:
        print(f'{produtos_preços[pos]:.<30}', end='')
    else:
        print(f'R${produtos_preços[pos]:>7.2f}')
print('-' * 40)