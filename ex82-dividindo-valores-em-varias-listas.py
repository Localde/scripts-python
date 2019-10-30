lista1 = []
lista2 = []
lista3 = []

while True:
    number = int(input('Digite um numero: '))
    lista1.append(number)
    if number % 2 == 0:
        lista2.append(number)
    else:
        lista3.append(number)
    escolha = str(input('Deseja continuar?[s][n] ')).lower()
    if escolha == 's':
        continue
    else:
        print(lista1)
        print(lista2)
        print(lista3)
        break
