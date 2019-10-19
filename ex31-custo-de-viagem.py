distancia = float(input('Qual é a distância da viagem em km? '))

print(f'Valor da passagem: R${distancia * 0.5:.2f}.' if distancia <= 200 else f'Valor da passagem: R${distancia * 0.45:.2f}.')
