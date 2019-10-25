listagem = ('caneta', 'lapis', 'caderno', 'estojo', 'apontador')

for p in listagem:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')