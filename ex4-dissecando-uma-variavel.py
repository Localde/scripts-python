variavel = input('Digite algo: ')

print('Contém letras: {}'.format(variavel.isalpha()))
print('Só Contém letras Minusculas: {}'.format(variavel.islower()))
print('Só Contém letras Maiusculas: {}'.format(variavel.isupper()))
print('Só Contém numeros: {}'.format(variavel.isnumeric()))
print('É um titulo: {}'.format(variavel.istitle()))
