print('Escolha umas seguintes opções:')
print('[m] para masculino.')
print('[f] para feminino.')
escolha = str(input())

while not escolha == 'm' or escolha == 'f':
    escolha = str(input('Digite novamente: '))