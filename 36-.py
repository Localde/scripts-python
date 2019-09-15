preco = float(input('Quanto custa a casa? '))
salario = float(input('Quanto é seu salario? '))
tempo = int(input('Em quantos anos deseja pagar? '))
limite = salario * 0.3
parcela_mensal = preco / (tempo * 12)

if parcela_mensal <= limite:
    print('Você deve pagar R${:.2f} por mes durante {} meses'.format(parcela_mensal, tempo * 12))
else:
    print('O emprestimo foi negado')