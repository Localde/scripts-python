ano_de_nascimento = int(input('Que ano você nasceu? '))
idade = 2019 - ano_de_nascimento

if idade < 18:
    falta = 18 - idade
    print(f'Falta {falta} anos para se alistar.')
elif idade > 18:
    passou = idade - 18
    print(f'Passou {passou} anos do alistamento.')
else:
    print('Ja é hora de se alistar.')