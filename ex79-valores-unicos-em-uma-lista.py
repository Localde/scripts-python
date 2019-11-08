lista = []
while True:
    number = int(input('Digite um numero:'))
    if number in lista:
        continue
    else:
        lista.append(number)
    escolha = str(input('Deseja continuar: [s] ou [n]')).lower()
    if escolha == 's':
        continue
    else:
        print(lista)
        break