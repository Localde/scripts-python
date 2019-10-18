a_number = int(input('Digite um numero: '))
b_number = int(input('Digite outro numero: '))
c_number = int(input('Digite outro numero: '))

maior = a_number

if b_number > c_number and b_number > maior:
    maior = b_number
elif c_number > b_number and c_number > maior:
    maior = c_number

menor = a_number

if b_number < c_number and b_number < menor:
    menor = b_number
elif c_number < b_number and c_number < menor:
    menor = c_number

print(f'Maior: {maior}')
print(f'Menor: {menor}')