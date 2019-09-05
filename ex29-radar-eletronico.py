velocidade = int(input('Qual foi a velocidade do carro em Km? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado por excesso de velocidade!!!')
    print('E devera pagar R${:.2f}'.format(multa))
else:
    print('Boa Viagem!!!')
print('-=-' * 20)
print('FIM DO PROGRAMA')
