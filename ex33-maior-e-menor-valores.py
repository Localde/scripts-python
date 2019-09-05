anumber = int(input('Digite um numero: '))
bnumber = int(input('Digite outro numero: '))
cnumber = int(input('Digite outro numero: '))

if anumber > bnumber and anumber > cnumber:
    if bnumber > cnumber:
        print('Maior: {}'.format(anumber))
        print('Menor: {}'.format(cnumber))
    else:
        print('Maior: {}'.format(anumber))
        print('Menor: {}'.format(bnumber))
elif bnumber > anumber and bnumber > cnumber:
    if anumber > cnumber:
        print('Maior: {}'.format(bnumber))
        print('Menor: {}'.format(cnumber))
    else:
        print('Maior: {}'.format(bnumber))
        print('Menor: {}'.format(anumber))
else:
    if anumber > bnumber:
        print('Maior: {}'.format(cnumber))
        print('Menor: {}'.format(bnumber))
    else:
        print('Maior: {}'.format(cnumber))
        print('Menor: {}'.format(anumber))