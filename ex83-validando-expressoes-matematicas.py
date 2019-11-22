lista = []

expressão = str(input('Digite uma expressão: '))

for caractere in expressão:
    if caractere == '(':
        lista.append('(')
    elif caractere == ')':
        if '(' in lista:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('É uma expressão.')
else:
    print('Não é uma expressão.')