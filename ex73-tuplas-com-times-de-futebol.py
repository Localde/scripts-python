times = ('a01', 'b02', 'a03', 'c04', 'a05', 'd06', 'a07', 'e08', 'f09', 'a10', 'a11', 'a12', 'a13', 'a14', 'Chapecoense', 'a16', 'a17', 'a18', 'a19', 'a20')

print(f'Os cinco primeiros colocado são {times[:5]}')
print(f'Os ultimos 4 colocado são {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'Posição da Chapecoense: {times.index("Chapecoense") + 1}')

