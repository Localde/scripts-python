ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2019 - ano_de_nascimento

if idade <= 9:
    print('MIRIM', idade)
elif 9 < idade <= 14:
    print('INFANTIL', idade)
elif 14 < idade <= 19:
    print('JUNIOR', idade)
elif 19 < idade <= 20:
    print('SÊNIOR', idade)
else:
    print('MASTER', idade)