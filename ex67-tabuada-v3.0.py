while True:
    number = int(input('Digite um numero: '))
    number2 = 0
    if number < 0:
        break
    while number2 != 11:
        multiplicação = number * number2
        print(f'{number} x {number2} = {multiplicação}')
        number2 += 1
