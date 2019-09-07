passagem = float(input('Quantos Km sera percorrido? '))

preco = passagem * 0.5 if passagem <= 200 else passagem * 0.45

print('O preço da passagem sera de R${}'.format(preco))
