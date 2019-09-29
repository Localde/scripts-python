primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

novo_termo = 0
for cont in range(1, 11, razão):
    print(primeiro_termo + razão)