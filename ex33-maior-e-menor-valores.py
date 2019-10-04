maior = 0
menor = 1000
for rep in range(0, 3):
    number = int(input('Digite um numero: '))
    #verifica maior
    if number > maior:
        maior = number
    #verifica menor
    if number < menor:
        menor = number
print(f'Maior: {maior}')
print(f'Menor: {menor}')
