frase = str(input('Digite uma frase: ')).strip().lower()

print(f'Letra [A] aparece {frase.count("a")} vezes')
print(f'A primeira vez em que ela aparece é na {frase.find("a") + 1} posição.')
print(f'A ultima vez em que ela aparece é na {frase.find("a") + 1} posição.')