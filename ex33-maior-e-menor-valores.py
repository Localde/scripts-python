a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))

#Faça da forma mais dificil depois simplifique da forma mais lógica.

maior = a

if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c

menor = a

if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

print(f'Maior: {maior}')
print(f'Menor: {menor}')