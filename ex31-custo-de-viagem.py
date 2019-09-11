km = float(input('Digite quantos Kilometros ira percorrer?'))
print('Você ira pagar {} pela passagem.'.format(km * 0.5) if km > 200 else 'Você ira pagar {} pela passagem.'.format(km * 0.45))
