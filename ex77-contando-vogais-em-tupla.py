palavras = 'Caderno', 'Caneta', 'Lapis'

for palavra in palavras:
    print(f'{palavra}: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end='')
    print('\n')
