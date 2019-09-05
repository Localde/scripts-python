salario = float(input('Qual é seu salario? '))

if salario > 1250:
    newsalario = salario + (salario * 0.1)
    print('Seu novo salario é de R${:.2f}.'.format(newsalario))
else:
    newsalario = salario + (salario * 0.15)
    print('Seu novo salario é de R${:.2f}.'.format(newsalario))
