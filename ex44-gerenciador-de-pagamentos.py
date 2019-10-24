preço_do_produto = float(input('Digite o preço do produto: '))

print("""Escolha uma das opções abaixo:
[1]- Á vista dinheiro/cheque: 10% de desconto
[2]- Á vista no cartão: 5% de desconto
[3]- Em até 2x no cartão: preço normal
[4]- 3x ou mais no cartão: 20% de juros.
""")
escolha = int(input())

if escolha == 1:
    print(f'{preço_do_produto * 0.90}')
elif escolha == 2:
    print(f'{preço_do_produto * 0.95}')
elif escolha == 3:
    print(f'{preço_do_produto}')
elif escolha == 4:
    print(f'{preço_do_produto * 1.2}')
else:
    escolha = int(input())