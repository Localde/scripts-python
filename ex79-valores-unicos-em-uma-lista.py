lista = []

while True:
    numero = int(input('Digite um numero: '))
    if numero in lista:
        continue
    else:
        lista.append(numero)
    escolha = str(input('Deseja continuar? [s] = sim [n] = não\n')).lower()
    if escolha == 's':
        continue
    else:
        break
print(lista)