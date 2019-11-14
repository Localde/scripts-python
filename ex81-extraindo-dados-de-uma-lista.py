lista_de_numeros = []
quantidade_de_numeros_digitados = 0
while True:
    lista_de_numeros.append(int(input('Digite um numero: ')))
    quantidade_de_numeros_digitados += 1
    escolha = str(input('Deseja continuar? [s] ou [n]'))
    if escolha == 'n':
        print(f'Quantidade de numeros digitados: {quantidade_de_numeros_digitados}')
        if 5 in lista_de_numeros:
            print(f'O 5 está na lista.')
        else:
            print(f'O 5 não está na lista.')
        lista_de_numeros.sort(reverse=True)
        print(f'Lista na Ordem Decrescente: {lista_de_numeros}')
        break
    elif escolha == 's':
        continue
    else:
        print('Comando Inválido.')