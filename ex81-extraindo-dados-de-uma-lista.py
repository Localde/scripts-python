lista = []
cont = 0
while True:
    number = int(input('Digite um numero: '))
    lista.append(number)
    cont += 1
    escolha = str(input('Deseja continuar [s] sim ou [n] não: ')).lower()
    if escolha == 's':
        continue
    elif escolha == 'n':
        print(f'Foram digitados {cont} numeros.')
        break
    else:
        print('Comando invalido')
lista.sort(reverse=True)
print(f'{lista}')
if 5 in lista:
    print('O numero 5 esta na lista.')
else:
    print('O numero 5 não esta na lista.')