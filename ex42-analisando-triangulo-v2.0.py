alado = int(input('Digite o valor do lado A: '))
blado = int(input('Digite o valor do lado B: '))
clado = int(input('Digite o valor do lado C: '))

if alado >= blado and alado >= clado and blado + clado >= alado or blado >= alado and blado >= clado and alado + clado >= blado or clado >= alado and clado >= blado and alado + blado >= clado:

    if alado == blado and alado == clado:
        print('É um Triângulo Equilátero.')
    elif alado == blado and alado != clado or blado == clado and blado != alado or clado == alado and clado != blado:
        print('É um Triângulo Isósceles.')
    else:
        print('É um Triângulo Escaleno.')

else:
    print('Não é um triângulo.')
