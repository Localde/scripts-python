anumber = int(input('Digite um numero inteiro: '))
bnumber = int(input('Digite outro numero inteiro: '))

if anumber > bnumber:
    print('O numero {} é maior que {}.'.format(anumber, bnumber))
elif bnumber > anumber:
    print('O numero {} é maior que {}.'.format(bnumber, anumber))
else:
    print('Não existe valor maior, os dois são iguais.')
