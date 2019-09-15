distancia = float(input('Digite a distancia em km do seu destino: '))

if distancia <= 200:
    print('Valor da Passagem: R${:.2f}'.format(distancia * 0.5))
else:
    print('Valor da Passagem: R${:.2f}'.format(distancia * 0.45))