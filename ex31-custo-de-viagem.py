km = float(input('Quantos Kilometros de distância? '))

print('Valor Cobrado: R${:.2f}'.format(km * 0.50) if km <= 200 else 'Valor Cobrado: R${:.2f}'.format(km * 0.45))
