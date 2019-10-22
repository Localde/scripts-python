fim = cont = soma = menor = 0
while True:
    nome_do_produto = str(input('Qual é o nome do produto? '))
    preço_do_produto = float(input('Qual é o preço do produto? '))
    soma += preço_do_produto

    if fim == 0:
        menor = preço_do_produto
        barato = nome_do_produto
        fim += 1
    elif preço_do_produto < menor:
        menor = preço_do_produto
        barato = nome_do_produto

    if preço_do_produto > 1000:
        cont += 1

    opção = str(input('Deseja continuar [s][n]? '))
    if opção == 's':
        continue
    elif opção == 'n':
        break
    else:
        print('Essa opção é invalida')

print(f'Total gasto na compra: R${soma:.2f}')
print(f'Quant. de produtos que custam mais de R$1000.00: {cont}')
print(f'O produto mais barato é o {barato}')