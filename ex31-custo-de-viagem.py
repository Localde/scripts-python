km = float(input('Qual é a distância da viajem em KM? '))

print(f'{km * 0.5:.2f}' if km <= 200 else f'{km * 0.45:.2f}')
