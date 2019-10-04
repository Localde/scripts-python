salario = float(input('Qual é seu salario: '))

print(f'Novo Salario: {salario * 1.10}' if salario > 1250 else f'Novo Salario: {salario * 1.15}')