preço_do_produto = float(input('Quanto custa o produto? '))
condição_de_pagamento = int(input("""
[1] - Á vista dinheiro/cheque: 10% de desconto
[2] - Á vista no cartão: 5% de desconto
[3] - Em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros.
"""))

if condição_de_pagamento == 1:
    print(f'R${preço_do_produto * 0.9:.2f}')
elif condição_de_pagamento == 2:
    print(f'R${preço_do_produto * 0.95:.2f}')
elif condição_de_pagamento == 3:
    print(f'R${preço_do_produto}')
elif condição_de_pagamento == 4:
    print(f'R${preço_do_produto * 1.2:.2f}')
else:
    print('Essa condição não é valida.')