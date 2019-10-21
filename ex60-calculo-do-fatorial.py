a = int(input('Digite um numero inteiro qualquer: '))
d = a
while True:
    b = a - 1
    d *= b
    a = b
    if b == 1:
        break
print(f'{d}')
