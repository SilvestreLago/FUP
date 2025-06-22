quant =  int(input())
matriz = []
for c in range(quant):
    lista = []
    for i in range(quant):
        lista.append(c*i)
    matriz.append(lista)

for j in range(quant):
    for k in range(quant):
        print(matriz[j][k], end=" ")
    print('')