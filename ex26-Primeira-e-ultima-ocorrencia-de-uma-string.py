frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece {} vezes.'.format(len(frase)))

print('A posição que aparece a primeira vez a letra A é a {} posição'.format(frase.find('a') + 1))

print('A ultima posição que aparece a letra A é a {} posição'.format(frase.rfind('a') + 1))
