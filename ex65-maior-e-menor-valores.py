opção = str('s')
soma = 0
media = 0
while opção != 'n':
    number = int(input('Digite um numero inteiro: '))
    maior = number
    menor = number
    opção = str(input('Deseja continuar? [s] or [n] '))
    if number >= maior and number >= menor:
        maior = number
    if number <= menor and number <= menor:
        menor = number
    soma += number
    media += 1
print(f'Média: {soma/media}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')