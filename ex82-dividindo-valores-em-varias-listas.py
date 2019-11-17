lista_contendo_todos_os_numeros = []
lista_contendo_os_numeros_pares = []
lista_contendo_os_numeros_impares = []
cont = 0
while True:
    lista_contendo_todos_os_numeros.append(int(input('Digite um numero: ')))
    if lista_contendo_todos_os_numeros[cont] % 2 == 0:
        lista_contendo_os_numeros_pares.append(lista_contendo_todos_os_numeros[cont])
    elif lista_contendo_todos_os_numeros[cont] % 2 != 0:
        lista_contendo_os_numeros_impares.append(lista_contendo_todos_os_numeros[cont])
    escolha = str(input('Deseja continuar? [s][n]')).lower().strip()
    if escolha == 's':
        cont += 1
        continue
    elif escolha == 'n':
        print(f'Lista com todos os numeros digitados: {lista_contendo_todos_os_numeros}')
        print(f'Lista contendo todos os numeros pares: {lista_contendo_os_numeros_pares}')
        print(f'Lista contendo todos os numeros impares: {lista_contendo_os_numeros_impares}')
        break
    else:
        print('Comando Inválido')
        break