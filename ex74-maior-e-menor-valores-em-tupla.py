from random import randint

a = randint(0, 5)
b = randint(0, 5)
c = randint(0, 5)
d = randint(0, 5)
e = randint(0, 5)

if a >= b and a >= c and a >= d and a >= e:
    maior = a
elif b >= a and b >= c and b >= d and b >= e:
    maior = b
elif c >= a and c >= b and c >= d and c >= e:
    maior = c
elif d >= a and d >= b and d >= c and d >= e:
    maior = d
elif e >= a and e >= b and e >= c and e >= d:
    maior = e

if a <= b and a <= c and a <= d and a <= e:
    menor = a
elif b <= a and b <= c and b <= d and b <= e:
    menor = b
elif c <= a and c <= b and c <= d and c <= e:
    menor = c
elif d <= a and d <= b and d <= c and d <= e:
    menor = d
elif e <= a and e <= b and e <= c and e <= d:
    menor = e

aleatorio = (a, b, c, d, e)
print(aleatorio)
print(f'Maior: {maior}')
print(f'Menor: {menor}')
