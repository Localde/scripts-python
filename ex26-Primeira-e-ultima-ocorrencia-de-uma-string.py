frase = str(input('Digite uma frase: ')).strip().lower()

print(f'A letra A aparece {frase.count("a")} vezes.')
print(f'A primeira vez que aparece é na {frase.find("a") + 1} posição.')
print(f'A ultima vez que aparece é na {frase.rfind("a") + 1} posição.')