km = int(input('Qual é a distancia da viagem em km? '))

if km <= 200:
    print(f'O valor da passagem é de R${km * 0.5:.2f}')
else:
    print(f'O valor da passagem é de R${km * 0.45:.2f}')
