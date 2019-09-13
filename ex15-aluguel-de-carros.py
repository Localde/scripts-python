dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foi rodado? '))

print('Você deve pagar R${:.2f}'.format((dias * 60) + (km * 0.15)))
