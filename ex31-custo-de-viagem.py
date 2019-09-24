km = float(input('How many kilometers will be traveled?'))

if km <= 200:
    print('The ticket costs {} dollars.'.format(km * 0.5))
else:
    print('The ticket costs {} dolars.'.format(km * 0.45))
