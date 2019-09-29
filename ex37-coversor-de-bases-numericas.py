number = int(input('Digite um numero inteiro qualquer: '))

print('Escolha uma das seguintes opções: ')
print('Digite 1 para binário.')
print('Digite 2 para octal.')
print('Digite 3 para hexadecimal.')

escolha = str(input())

if escolha == '1':
    print(f'{bin(number)[2:]}')
elif escolha == '2':
    print(f'{oct(number)[2:]}')
elif escolha == '3':
    print(f'{hex(number)[2:]}')
else:
    print('Esta opção não é válida.')
