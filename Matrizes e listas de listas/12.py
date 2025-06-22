matriz = []
for c in range(4):
    lista = []
    for i in range(4):
        lista.append(int(input()))
    matriz.append(lista)

for x in range(4):
    for y in range(4):
        print(matriz[y][x], end=" ")
    print('')