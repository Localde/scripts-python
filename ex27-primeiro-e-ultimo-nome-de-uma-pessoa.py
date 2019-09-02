nome = str(input('Escreva o nome completo de uma pessoa: ')).strip()

separar = nome.split()

print('O primeiro nome é {}'.format(separar[0]))
print('O ultimo nome é {}'.format(separar[len(separar)-1]))
