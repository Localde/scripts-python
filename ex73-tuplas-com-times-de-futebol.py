tupla = 'Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Grêmio', 'Internacional', 'Corinthians', 'Athletico-PR', 'Bahia', 'Goiás', 'Vaco da Gama', 'Fortaleza', 'Atlético', 'Botafogo', 'Ceará-SC', 'Cruzeiro', 'Fluminense', 'CSA', 'Chapecoense', 'Avai'

print(f'Os cinco primeiro colocado: {tupla[:5]}')
print(f'Os ultimos 4 colocados da tabela: {tupla[-4:]}')
print(f'Posição da Chapecoense: {tupla.index("Chapecoense") + 1}')