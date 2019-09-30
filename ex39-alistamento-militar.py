ano = int(input('Em que ano você nasceu? '))
idade = 2019 - ano

if idade == 18:
    print('Ja é hora de se alistar.')
elif idade > 18:
    print('Ja passou o tempo de se alistar.')
else:
    print('Não é hora de se alistar.')