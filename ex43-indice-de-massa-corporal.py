peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))

imc = peso / (altura * altura)

#if imc < 18.5:
#    print('Abaixo do Peso.')
#elif imc >= 18.5 and imc < 25:
#    print('Peso Ideal')
#elif imc >= 25 and imc <= 30:
#    print('Sobrepeso')
#elif imc > 30 and imc <= 40:
#    print('Obesidade')
#else:
#    print('Obesidade Mórbida')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você esta na faixa de peso normal')
elif 25 <= imc < 30:
    print('Você esta em Sobrepeso')
elif 30 <= imc < 40:
    print('Voce esta em Obesidade.')
else:
    print('Voce esta em Obesidade Mórbida.')
