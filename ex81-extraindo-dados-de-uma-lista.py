lista = []

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    escolha = str(input('Deseja continuar? [s]or[n] ')).lower()
    if escolha == 'n':
        break
    elif escolha == 's':
        continue
    else:
        print('Comando Inválido.')
lista.sort(reverse=True)
if 5 in lista:
    print('O 5 está na lista.')
else:
    print('O 5 não está na lista.')
print(f'Quantidade de números digitados: {len(lista)}')
print(f'Lista em Ordem decrescente: {lista}')