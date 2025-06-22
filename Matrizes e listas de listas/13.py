matriz = []
fim = [0, 0, 0, 0, 0]

for c in range(5):
    lista = []
    for i in range(5):
        lista.append(int(input()))
    matriz.append(lista)

for j in range(5):
    for k in range(5):
        fim[k] += matriz[j][k]

print(fim)