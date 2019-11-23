lista = []

for valores in range(1, 6):
    numero = int(input(f'{valores})Digite um valor: '))
    lista.append(numero)
    if valores == 1:
        maior = numero
        pos_maior = valores
        menor = numero
        pos_menor = valores
    elif numero > maior:
        maior = numero
        pos_maior = valores
    elif numero < menor:
        menor = numero
        pos_menor = valores
print(f'Numero maior: {maior} Posição: {pos_maior}')
print(f'Numero menor: {menor} Posição: {pos_menor}')