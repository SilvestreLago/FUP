cont = 0

arquivo = open(input(), "r")
letraI = input()

conteudo = arquivo.read()
arquivo.close()

for letra in conteudo:
    if letra == letraI:
            cont += 1

print(cont)