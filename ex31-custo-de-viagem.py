km = float(input('Qual é a distância da viagem? '))

if km <= 200:
    print(f'{km * 0.5:.2f}')
else:
    print(f'{km * 0.45:.2f}')