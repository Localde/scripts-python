# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 1000
for pessoas in range(1, 6):
    peso = float(input('Qual é seu peso? '))
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso
print(f'Maior: {maior}')
print(f'Menor: {menor}')

