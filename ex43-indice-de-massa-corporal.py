altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))

imc = peso / (altura ** 2)

if 18.5 > imc:
    print('Abaixo do peso.')
elif 18.5 < imc <= 25:
    print('Peso Ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesidade.')
elif 40 < imc:
    print('Obesidade Mórbida.')