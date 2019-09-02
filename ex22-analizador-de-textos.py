nome = str(input('Digite seu nome completo: ')).strip()

print('Todas as letras maiusculas: {}'.format(nome.upper()))
print('Todas as letras minusculas: {}'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome) - nome.count(' ')))

separar = nome.split()

print('Quantas letras tem o primeiro nome: {}'.format(len(separar[0])))
