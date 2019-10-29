lista = []

while True:
    number = int(input('Digite um numero: '))
    if number in lista:
        continue
    else:
        lista.append(number)

    escolha = str(input('Deseja escolher mais um numero?[s][n] '))
    if escolha == 's':
        continue
    else:
        print(f'{sorted(lista)}')
        break
