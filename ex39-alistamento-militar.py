ano_de_nascimento = int(input('Em que ano você nasceu? '))
idade = 2019 - ano_de_nascimento

if idade < 18:
    tempo = 18 - idade
    print(f'Falta {tempo} anos para se alistar!')
elif idade == 18:
    print('Ja é hora de se alistar!')
else:
    tempo = idade - 18
    print(f'Ja passou {tempo} anos do tempo de alistamento!')