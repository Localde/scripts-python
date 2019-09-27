km = int(input('Qual é a velocidade do carro? '))

if km > 80:
    print(f'Você foi multado e deve pagar: R${7 * (km - 80):.2f}')
else:
    print('Boa Viagem!')
