lista = []
a = 0
while True:
    lista.append(int(input('Digite um numero: ')))
    a += 1
    escolha = str(input('Deseja continuar?[s][n] '))
    if escolha == 's':
        continue
    else:
        lista.sort(reverse=True)
        b = lista
        print(f'Foram digitados {a} numeros.')
        print(f'Ordem decrescente: {b}')
        if 5 in lista:
            print('O valor 5 foi digitado.')
        else:
            print('O valor 5 não foi digitado.')
        break