salario = float(input('Qual é seu salario? '))
print('Com um aumento de 10% vc recebera R${:.2f}'.format(salario * 1.1) if salario > 1250 else 'Com um aumento de 15% vc recebera R${:.2f}'.format(salario * 1.15))
