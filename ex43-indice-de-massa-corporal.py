#peso = float(input('Qual é seu peso? '))
#altura = float(input('Qual a sua altura? '))

#imc = peso / (altura ** 2)
imc = 25
if imc <= 18.5:
    print(f'Abaixo do peso pois seu imc é de {imc}.')
elif 18.5 < imc <= 25:
    print(f'Peso Ideal pois seu imc é de {imc}.')
elif 25 < imc <= 30:
    print(f'Sobrepeso pois seu imc é de {imc}.')
elif 30 < imc <= 40:
    print(f'Obesidade pois seu imc é de {imc}.')
else:
    print(f'Obesidade Mórbida pois seu imc é de {imc}.')