dias = int(input('\033[1;31mQuantos dias o carro andou? '))
km = float(input('\033[1;32mQuantos km o carro andou? '))

print('\033[1;34mDeve pagar \033[1;30mR${:.2f}'.format((60 * dias) + (0.15 * km)))
