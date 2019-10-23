a_number = int(input('Digite um numero: '))
b_number = int(input('Digite outro numero: '))
c_number = int(input('Digite outro numero: '))
d_number = int(input('Digite outro numero: '))

tupla = (a_number, b_number, c_number, d_number)
a = 0
while a < 4:
    if tupla[a] % 2 == 0:
        print(f'{tupla[a]}\n', end='')
    a += 1

print(f'O numero 9 aparece {tupla.count(9)} vezes.')
print(f'O numero 3 aparece pela primeira vez na {tupla.index(3) + 1} posição.')
