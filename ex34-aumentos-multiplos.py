salario = float(input('Qual é o seu salario? '))
print('Com um aumento de 10% seu salario é de R${:.2f}'.format(salario * 1.1) if salario > 1250 else 'Com um aumento de 15% seu salario é de R${:.2f}'.format(salario * 1.15))
