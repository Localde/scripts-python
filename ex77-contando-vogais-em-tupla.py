#toda palavra é uma lista de letras.
palavras = 'carro', 'moto', 'bicicleta'

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

