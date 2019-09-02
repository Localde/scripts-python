frase = str(input('Escreva uma frase: ')).strip().lower()

print('Quantas vezes aparece a letra A: {}'.format(frase.count('a')))
print('Em que posição ela aparece a primeira vez: {}'.format(frase.find('a')+1))
print('Em que posição ela aparece a última vez: {}'.format(frase.rfind('a')-1))