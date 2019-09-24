phrase = str(input('Enter a sentence: ')).strip().lower()

contador = phrase.count('a')
print('The letter A appears {} times.'.format(contador))

first_order = phrase.find('a') + 1
print('The letter A appears for the first time in the {} order.'.format(first_order))

last_order = phrase.rfind('a') + 1
print('The letter A appears for the last time in the {} order.'.format(last_order))