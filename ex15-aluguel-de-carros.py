dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kilometros Rodado? '))
resultado = km * 0.15 + dias * 60
print('Deve pagar R${:.2f}.'.format(resultado))
