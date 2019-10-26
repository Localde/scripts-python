#5! = 5 * 4 * 3 * 2 * 1 = 120

number = int(input('Digite um numero inteiro: '))
b = a = number
while True:
    a -= 1
    c = a * b
    b = c
    if a == 1:
        print(f'{c}')
        break