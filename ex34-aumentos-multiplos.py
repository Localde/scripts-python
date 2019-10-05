salario = float(input('Qual é seu salario: '))
print(f'Seu novo salario é de R${salario * 1.1:.2f}' if salario > 1250 else f'Seu novo salario é de R${salario * 1.15:.2f}')