lista = []
cont = 0
while True:
    lista.append(int(input('Digite um numero: ')))
    cont += 1
    escolha = str(input('Digite [s] para continuar ou [n] para parar: '))
    if escolha == 's':
        continue
    elif escolha == 'n':
        break
    else:
        print('Opção Invalida.')
lista.sort(reverse=True)
print(f'Foi digitado {cont} numeros.')
print(f'Lista Ordemanda: {lista}')
if 5 in lista:
    print('A lista possui o numero 5.')

else:
    print('A lista não possui o numero 5.')