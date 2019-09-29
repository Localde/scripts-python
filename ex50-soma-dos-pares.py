soma = 0
for ler in range(1, 7):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        soma += numero
print(soma)