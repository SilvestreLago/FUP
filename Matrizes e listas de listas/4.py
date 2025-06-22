matriz = []
maior = -99999999999999999999999999999999999999999999999999999999999999999999999
x = 0
y = 0

for c in range(4):
    lista = []
    for i in range(4):
        lista.append(int(input()))
    matriz.append(lista)

for j in range(4):
    for k in range(4):
        num = matriz[j][k]
        if num > maior:
            maior = num
            x = j
            y = k        

for q in range(4):
    for w in range(4):
        print(matriz[q][w], end=" ")
    print('')
print(x)
print(y)
print(maior)