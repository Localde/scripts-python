ano = int(input('Enter a year: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('É bissexto.')
elif ano % 400 == 0:
    print('É bissexto.')
else:
    print('Não é bissexto.')