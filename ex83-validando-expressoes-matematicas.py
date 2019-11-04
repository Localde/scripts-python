#Em uma expressão quando se abre um parenteses tem que fecha-lo.
#toda string é uma lista.
expr = str(input('Digite uma expressão:'))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta.')
else:
    print('Sua expressão esta errada.')
