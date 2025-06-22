matriz1 = []
matriz2 = []
matriz3 = []

for c in range(4):
    lista1 = []
    for i in range(4):
        lista1.append(int(input()))
    matriz1.append(lista1)

for j in range(4):
    lista2 = []
    for k in range(4):
        lista2.append(int(input()))
    matriz2.append(lista2)

for q in range(4):
    lista3 = []
    for w in range(4):
        valorL1 = matriz1[q][w]
        valorL2 = matriz2[q][w]
        if valorL1 >= valorL2:
            lista3.append(valorL1)
        else:
            lista3.append(valorL2)
    matriz3.append(lista3)

for x in range(4):
    for y in range(4):
        print(matriz3[x][y], end=" ")
    print('')