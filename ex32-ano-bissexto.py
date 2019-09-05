from datetime import date

ano = int(input('Digite um ano qualquer ou coloque 0 para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year

#if ano % 4 == 0:
    #if ano % 100 != 0:
        #print('O ano é Bissexto')
    #else:
        #print('O ano não é Bissexto!')
#else:
    #if ano % 400 == 0:
        #print('O ano é Bissexto')
    #else:
        #print('O ano não é Bissexto')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
