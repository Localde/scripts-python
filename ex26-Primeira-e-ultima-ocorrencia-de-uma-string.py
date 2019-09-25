phrase = str(input('Enter a sentence:')).strip().lower()

print('A letra A aparece {} vezes.'.format(phrase.count('a')))
print('A letra A aparece pela primeira vez na {} posição.'.format(phrase.find('a') + 1))
print('A letra A aparece pela ultima vez na {} posição.'.format(phrase.find('a') + 1))
