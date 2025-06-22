matriz = []
for i in range(10):
    lista = []
    for j in range(10):
        if i< j:
            lista.append(2 * i + 7 * j - 2)
        elif i == j:
            lista.append(3 * i ** 2 - 1)
        elif i>j:
            lista.append( 4 * i ** 3 - 5 * j ** 2 + 1)
    matriz.append(lista)

for x in range(10):
    for y in range(10):
        print(matriz[x][y], end=" ")
    print('')