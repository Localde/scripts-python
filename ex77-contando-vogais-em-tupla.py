palavras = 'Ollywer', 'Gabriel', 'Weliton', 'Alexandre'

for palavra in palavras:
    print(f'{palavra}: ', end='')
    for letra in palavra:
        if letra in 'aeiouAEIOU':
           print(letra, end=' ')
        else:
            continue
    print('\n')