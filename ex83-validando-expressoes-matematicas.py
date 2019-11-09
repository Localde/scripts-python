#lista = []

expressão = str(input('Digite uma expressão: '))
cont = 0
cont2 = 0
for simb in expressão:
    if simb == '(':
        #lista.append('(')
        cont += 1
    if simb == ')':
        #lista.append('(')
        cont2 += 1
if cont == cont2:
    print('A expressão esta correta.')
else:
    print('A expressão esta incorreta')