variavel = input('\033[0;35mDigite algo: ')

print('\033[1;36mé espaço: \033[1;32m{}'.format(variavel.isspace()))
print('\033[1;37mé numero: \033[1;32m{}'.format(variavel.isnumeric()))
print('\033[1;30mé minusculo: \033[1;32m{}'.format(variavel.islower()))
print('\033[1;31mé maiusculo: \033[1;32m{}'.format(variavel.isupper()))
print('\033[1;32mé titulo: \033[1;32m{}'.format(variavel.istitle()))
print('\033[1;33mé letra: \033[1;32m{}'.format(variavel.isalpha()))
