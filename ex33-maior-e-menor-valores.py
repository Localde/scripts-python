a_number = int(input('Digite um numero inteiro: '))
b_number = int(input('Digite outro numero inteiro: '))
c_number = int(input('Digite outro numero inteiro: '))

maior = a_number

if b_number > c_number and b_number > maior:
    maior = b_number
elif c_number > b_number and c_number > maior:
    maior = c_number

print(f'Maior: {maior}')

menor = a_number

if b_number < c_number and b_number < maior:
    menor = b_number
elif c_number < b_number and c_number < maior:
    menor = c_number

print(f'Menor: {menor}')


