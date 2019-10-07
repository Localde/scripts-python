a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'Maior: {maior}')
print(f'Menor: {menor}')
