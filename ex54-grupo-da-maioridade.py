maioridade = 0
menoridade = 0
for pessoas in range(1, 8):
    ano_de_nascimento = int(input('Digite o ano de nascimento: '))
    if ano_de_nascimento <= 2001:
        maioridade += 1
    else:
        menoridade += 1
print(f'Adultos: {maioridade}')
print(f'Jovens: {menoridade}')