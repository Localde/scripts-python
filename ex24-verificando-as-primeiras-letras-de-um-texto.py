nome_da_cidade = str(input('Digite o nome da cidade: ')).strip().lower()
dividir = nome_da_cidade.split()
print('É verdade que o nome da cidade começa com Santo.' if dividir[0] == 'santo' else 'É falso que o nome da cidade começa com Santo.')