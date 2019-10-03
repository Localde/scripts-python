soma = 0
media = 0
maior_idade = 0
nome_do_mais_velho = str()
contagem_de_mulheres = 0
for pessoas in range(1, 5):
    nome = str(input('Qual é seu nome? '))
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Digite [m] para Masculino ou [f] para Feminino:'))
    soma += idade
    media = soma / 4
    if idade > maior_idade and sexo == 'm':
        maior_idade = idade
        nome_do_mais_velho = nome
    if sexo == 'f' and idade < 20:
        contagem_de_mulheres += 1
print(f'A média de idade do grupo: {media}')
print(f'O nome do homem mais velho é {nome_do_mais_velho}')
print(f'{contagem_de_mulheres} mulheres tem menos de vinte anos.')