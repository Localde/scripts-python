lista1 = []
lista2 = []
lista3 = []
fim = 2
for cont in range(0, fim):
    lista1.append(int(input('Digite um numero: ')))
    if lista1[cont] % 2 == 0:
        lista2.append(lista1[cont])
    else:
        lista3.append(lista1[cont])
    fim = int(input('Deseja continuar?[1 = Sim][0 = Não] '))
    if fim == 0:
        continue
    else:
        fim += 1
print(f'Lista Completa: {lista1}')
print(f'Lista par: {lista2}')
print(f'Lista impar: {lista3}')