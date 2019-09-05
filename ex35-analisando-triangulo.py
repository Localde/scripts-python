alado = int(input('Qual é o tamanho do lado A do Triângulo? '))
blado = int(input('Qual é o tamanho do lado B do Triângulo? '))
clado = int(input('Qual é o tamanho do lado C do Triângulo? '))

#Condições:

#1º A soma de dois lados menores tem que ser igual ou maior do que o 3ºlado.

#verificando lado maior.
if alado >= blado and alado >= clado:
    if (blado + clado) >= alado:
        print('É um triângulo')
    else:
        print('Não é um triângulo')
elif blado >= alado and blado >= clado:
    if (alado + clado) >= blado:
        print('É um triângulo')
    else:
        print('Não é um triângulo')
elif clado >= alado and clado >= blado:
    if (blado + alado) >= clado:
        print('É um triângulo')
    else:
        print('Não é um triângulo')