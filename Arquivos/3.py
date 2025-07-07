cont = 0
vogais = ['a', 'A', 'e', 'E', 'i', "I",'o', 'O', 'u', 'U']

arquivo = open(input(), "r")

conteudo = arquivo.read()
arquivo.close()

for letra in conteudo:
    for vogal in vogais:
        if letra == vogal:
            cont += 1

print(cont)