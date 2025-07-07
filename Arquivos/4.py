contV = 0
contC = 0
vogais = ['a', 'A', 'e', 'E', 'i', "I",'o', 'O', 'u', 'U']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n', 'p','q', 'r', 's', 't', 'v', 'w','x', 'y', 'z','B', 'C', 'D', 'F', 'G', 'H','J', 'K', 'L', 'M', 'N', 'P','Q', 'R', 'S', 'T', 'V', 'W','X', 'Y', 'Z']
arquivo = open(input(), "r")

conteudo = arquivo.read()
arquivo.close()

for letra in conteudo:
    for vogal in vogais:
        if letra == vogal:
            contV += 1
    for consoante in consoantes:
        if letra == consoante:
            contC += 1   
print(contV)
print(contC)