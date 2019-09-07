alado = int(input('Digite o valor do lado A: '))
blado = int(input('Digite o valor do lado B: '))
clado = int(input('Digite o valor do lado C: '))

print('É UM TRIÂNGULO' if alado >= blado and alado >= clado and (blado + clado) >= alado or blado >= alado and blado >= clado and (alado + clado) >= blado or clado >= alado and clado >= blado and (alado + blado) >= clado else 'NÃO É UM TRIÂNGULO')