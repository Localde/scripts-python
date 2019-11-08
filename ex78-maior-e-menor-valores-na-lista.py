lista = []
for pos in range(1, 6):
    number = int(input('Digite um numero: '))
    if pos == 1:
        maior = number
        menor = number
    elif number > maior:
        maior = number
        pos_maior = pos
    elif number < menor:
        menor = number
        pos_menor = pos
    lista.append(number)
print(f'Maior: {maior} na {pos_maior} posição.')
print(f'Menor: {menor} na {pos_menor} posição.')