valor_da_casa = float(input('Quanto custa a casa? '))
salario = float(input('Qual é o seu salario? '))
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestacao_mensal = (valor_da_casa / anos) / 12
limite = salario * 0.3

if prestacao_mensal <= limite:
    print(f'O valor a pagar é de {prestacao_mensal:.2f}')
else:
    print(f'O emprestimo foi negado pois ultrapassou o limite de 30%.')