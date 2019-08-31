nome = str(input('Digite o nome completo de uma pessoa: ')).strip()
n = nome.split()
print('Primeiro: {}'.format(n[0]))
print('Ultimo: {}'.format(n[len(n)-1]))
