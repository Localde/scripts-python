peso = float(input('Qual é seu peso? '))
altura = float(input('Qual a sua Altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc} e por causa disso você esta abaixo do peso ideal.')
elif 25 > imc >= 18.5:
    print(f'Seu IMC é {imc} e por causa disso você esta no peso ideal.')
elif 25 <= imc <= 30:
    print(f'Seu IMC é {imc} e por causa disso você esta em sobrepeso.')
elif 30 <= imc <= 40:
    print(f'Seu IMC é {imc} e por causa disso você esta em obesidade.')
else:
    print(f'Seu IMC é {imc} e por causa disso você esta em obesidade mórbida.')
