maior_de_18 = homens = mulher_menor_de_20 = 0
while True:
    sexo = str(input('Qual é o seu sexo? [m][f] '))

    if sexo == 'm':
        idade = int(input('Qual a sua idade? '))
        homens += 1
        if idade > 18:
            maior_de_18 += 1
    if sexo == 'f':
        idade = int(input('Qual a sua idade? '))
        if idade < 20:
            mulher_menor_de_20 += 1
        if idade > 18:
            maior_de_18 += 1

    escolha = str(input('Deseja continuar? [s][n]'))
    if escolha == 'n':
        break

print(f'{maior_de_18} tem mais de 18 anos.')
print(f'{homens} homem(ns) foram cadastrados.')
print(f'{mulher_menor_de_20} mulher(es) tem menos de 20 anos.')