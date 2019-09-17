day = int(input('How many days was the car rended? '))
km = float(input('How many kilometers was it run? '))

print('You must pay ${:.2f} Dollars.'.format((60 * day) + (km * 0.15)))
