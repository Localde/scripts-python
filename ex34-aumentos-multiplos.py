salario = float(input('Qual é o seu salario: '))

if salario <= 1250:
    print(f'Seu novo salario com aumento é de {salario * 1.15:.2f}')
else:
    print(f'Seu novo salario com aumento é de {salario * 1.10:.2f}')