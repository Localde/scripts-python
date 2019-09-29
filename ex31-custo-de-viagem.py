km = float(input('Qual é a distância em Km: '))

if km <= 200:
    print(f'O valor da passagem é de R${km * 0.5:.2f}')
else:
    print(f'O valor da passagem é de R${km * 0.45:.2f}')
