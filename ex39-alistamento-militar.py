ano_de_nascimento = int(input('Digite o ano que você nasceu: '))
idade = 2019 - ano_de_nascimento

if idade < 18:
    print(f'Falta {18 - idade} anos para se alistar.')
elif idade > 18:
    print(f'Passou {idade - 18} anos para se alistar.')
else:
    print(f'Ja é hora de se alistar.')