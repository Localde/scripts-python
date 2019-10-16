primeiro_termo = int(input('Qual é o primeiro termo? '))
razão = int(input('Qual é a razão? '))
cont = 0
cont2 = 10
while cont != cont2:
    primeiro_termo += razão
    print(primeiro_termo)
    if cont == cont2 - 1:
        cont2 = int(input('Quantos termos deseja continuar mostrando? ')) + 1
        if cont2 == 0:
            break
        cont = 0
    cont += 1
