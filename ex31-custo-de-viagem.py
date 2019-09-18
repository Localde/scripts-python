distance = float(input('How far is the trip?'))

if distance <= 200:
    print('The ticket will cost {} dollars.'.format(distance * 0.5))
else:
    print('The ticket will cost {} dollars.'.format(distance * 0.45))
