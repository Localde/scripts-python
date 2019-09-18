number = int(input('Enter a number: '))

if number == 0:
    print('The Number is Neutral.')
elif number % 2 == 0:
    print('It is pair..')
else:
    print('It is odd.')