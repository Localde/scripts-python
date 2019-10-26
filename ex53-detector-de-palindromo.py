frase = str(input('Digite algo: ')).strip().lower().split()
juntar = ''.join(frase)
inverso = ''
for cont in range(len(juntar) - 1, -1, -1):
    inverso += juntar[cont]
if inverso == juntar:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')