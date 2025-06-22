quant = int(input())
matriz = []
cont = 0
for c in range(quant):
    lista = []
    for i in range(quant):
        if cont == i:
            lista.append(1)
        else:
            lista.append(0)
    cont += 1
    matriz.append(lista)

for j in range(quant):
    for k in range(quant):
        print(matriz[j][k], end=" ")
    print('')