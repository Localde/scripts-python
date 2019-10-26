velocidade = int(input('Qual foi a velocidade: '))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print('Você foi multado.')
    print(f'Valor da Multa: R${multa:.2f}')
