dicionario = {}

nome = str(input('Qual é o seu nome? '))
media = float(input('Qual a sua média? '))

dicionario['nome'] = nome
dicionario['media'] = media

for a, b in dicionario.items():
    print(f'{a} = {b}')