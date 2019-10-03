from random import randint
print('[1]PEDRA\n[2]PAPEL\n[3]TESOURA\n')
escolha = int(input('Faça sua escolha: '))
maquina = randint(1, 3)
if escolha == 1 and maquina == 3 or escolha == 2 and maquina == 1 or escolha == 3 and maquina == 2:
    print('Voce Ganhou', maquina)
elif escolha == 3 and maquina == 1 or escolha == 1 and maquina == 2 or escolha == 2 and maquina == 3:
    print('Voce Perdeu', maquina)
else:
    print('Empatou!', maquina)