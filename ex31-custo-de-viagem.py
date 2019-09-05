distancia = int(input('Quantos km tem de viagem?'))

#if distancia <= 200:
    #valor = distancia * 0.50
    #print('O preço da passagem é de? R${:.2f}'.format(valor))
#else:
    #valor = distancia * 0.45
    #print('O preço da passagem é de? R${:.2f}'.format(valor))

valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('O valor da passagem é de R${:.2f}'.format(valor))