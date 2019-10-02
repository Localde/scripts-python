ano_atual = 2019
maior = 0
menor = 0
for pessoas in range(1, 8):
    ano = int(input('Em que ano você nasceu: '))
    idade = ano_atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Maior: {maior}')
print(f'Menor: {menor}')