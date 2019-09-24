product = float(input('What is the normal price of the product? '))

print('\nDigite 1 para Á VISTA DINHEIRO/CHEQUE: 10% de desconto.')
print('Digite 2 para Á VISTA NO CARTÃO: 5% DE DESCONTO.')
print('Digite 3 para EM ATÉ 2X NO CARTÃO: PREÇO NORMAL.')
print('Digite 4 para 3X OU MAIS NO CARTÃO: 20% DE JUROS.\n')
escolha = str(input())

if escolha == '1':
    print('Á VISTA DINHEIRO/CHEQUE: R${:.2f}'.format(product * 0.9))
elif escolha == '2':
    print('Á VISTA NO CARTÃO: R${:.2f}'.format(product * 0.95))
elif escolha == '3':
    print('EM ATÉ 2X NO CARTÃO: R${:.2f}'.format(product))
elif escolha == '4':
    print('3X OU MAIS NO CARTÃO: R${:.2f}'.format(product * 1.20))
else:
    print('Não existe esta opção.')