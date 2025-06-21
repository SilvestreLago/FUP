nome = input()
letras = []
for letra in nome:
    if letra.isalpha():
        existe = False
        for l in letras:
            if letra == l:
                existe = True
                break
        if not existe:
            letras.append(letra)
print(len(letras))