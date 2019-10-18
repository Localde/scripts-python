nome_completo = str(input('Digite seu nome completo: ')).lower()
verificar = 'silva' in nome_completo

print('Tem Silva no nome.' if verificar == 1 else 'Não tem Silva no nome.')
