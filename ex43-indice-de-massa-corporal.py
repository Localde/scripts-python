altura = float(input('Qual é a sua altura: '))
peso = float(input('Qual é o seu peso: '))
imc = peso / (altura ** 2)
#print(f'Seu IMC é de: {imc}')
if imc < 18.5:
    print('Esta abaixo do peso', imc)
elif 18.5 <= imc < 25:
    print('Peso Ideal', imc)
elif 25 <= imc < 30:
    print('Sobrepeso', imc)
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')