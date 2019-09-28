nome_da_cidade = str(input('Digite o nome da cidade: ')).strip().lower().split()

verifica = nome_da_cidade[0].find('santo')

if verifica == 0:
    print('Tem Santo no inicio.')
else:
    print('Não tem Santo no inicio.')


