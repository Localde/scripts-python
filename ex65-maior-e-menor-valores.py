escolha = 's'
media = rep = soma = maior = menor = 0

while escolha == 's':
    escolha = str(input('Deseja escolher um numero?[s][n] '))
    if escolha == 's':
        number = int(input('Digite um numero inteiro: '))
        rep += 1
        soma += number
        media = soma / rep
    if rep == 1:
        maior = number
        menor = number
    if number >= maior:
        maior = number
    if number <= menor:
        menor = number
print(f'Média: {media}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
