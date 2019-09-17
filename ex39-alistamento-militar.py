dia = int(input('Em que dia você nasceu? '))
mes = int(input('Em que mes você nasceu?'))
ano = int(input('Em que ano você nasceu?'))

#Com 18 anos ja é hora de se alistar
#Com menos de 18 anos ele ainda vai se alistar
#Com mais de 18 ja passou a hora de se alistar

if dia <= 16 and mes <= 9 and ano == 2001:
    print('Ja é hora de se alistar.')
elif ano > 2001:
    print('Ainda vai se alistar.')
elif dia > 16 and ano == 2001:
    print('Ainda vai se alistar.')
elif mes > 9 and ano == 2001:
    print('Ainda vai se alistar.')
elif ano < 2001:
    print('Ja passou a hora de se alistar.')
