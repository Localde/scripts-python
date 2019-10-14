primeiro_termo = int(input('Qual é o primeiro termo? '))
razao = int(input('Qual é a razão? '))
progressao = primeiro_termo
ultimo_termo = primeiro_termo + 10
while primeiro_termo != ultimo_termo:
    progressao += razao
    print(f'{progressao}')
    primeiro_termo += 1