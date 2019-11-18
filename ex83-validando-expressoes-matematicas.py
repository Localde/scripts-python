lista = []
exp = []

expressão = str(input('Digite uma expressão: '))
lista.append(expressão)
for caractere in lista:
    if caractere == '(':
        exp.append('(')
    else:
        if caractere == ')':
            exp.pop()
        else:
            exp.append(')')
if len(exp) == 0:
    print('É uma expressão.')
else:
    print('Não é uma expressão.')