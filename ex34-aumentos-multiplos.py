salario = float(input('Qual é seu salario? '))
print('Seu salario teve um aumento de 10% então você recebera R${:.2f}'.format(salario + (salario * 0.1)) if salario > 1250 else 'Seu salario teve um aumento de 15% então você recebera R${:.2f}'.format(salario + (salario * 0.15)))
