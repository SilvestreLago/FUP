matriz1 = []
matriz2 = []
matriz3 = []

for c in range(5):
    lista1 = []
    for i in range(5):
        lista1.append(int(input()))
    matriz1.append(lista1)

for j in range(5):
    lista2 = []
    for k in range(5):
        lista2.append(int(input()))
    matriz2.append(lista2)

for q in range(5):
    lista3 = []
    for w in range(5):
        soma = 0
        for l in range(5):
            soma += matriz1[q][l] * matriz2[l][w]
        lista3.append(soma)
    matriz3.append(lista3)

for x in range(5):
    for y in range(5):
        print(matriz3[x][y], end=" ")
    print('')