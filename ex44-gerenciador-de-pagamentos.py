valor_do_produto = float(input('Qual é o valor do produto? '))
print("""
[1] Á vista dinheiro/cheque: 10% de desconto
[2] Á vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4]- 3x ou mais no cartão: 20% de juros.
""")
forma_de_pagamento = int(input())

if forma_de_pagamento == 1:
    print(f'{valor_do_produto * 0.9:.2f}')
elif forma_de_pagamento == 2:
    print(f'{forma_de_pagamento * 0.95:.2f}')
elif forma_de_pagamento == 3:
    print(f'{forma_de_pagamento:.2f}')
elif forma_de_pagamento == 4:
    print(f'{forma_de_pagamento * 1.2:.2f}')