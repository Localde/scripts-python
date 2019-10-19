valor_da_casa = float(input('Quanto custa a casa? '))
salario_do_comprador = float(input('Qual é o seu salario? '))
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestação_mensal = valor_da_casa / (anos * 12)

limite = salario_do_comprador * 0.3

if prestação_mensal <= limite:
    print('O empréstimo foi aceito.')
else:
    print('O emprestimo foi negado.')