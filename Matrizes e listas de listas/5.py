matriz = []
x = -1
y = -1
for c in range(5):
    lista = []
    for i in range(5):
        lista.append(int(input()))
    matriz.append(lista)

valor = int(input())

for j in range(4):
    for k in range(4):
        num = matriz[j][k]
        if num == valor:
            x = j
            y = k
            break
    if x != -1 and y != -1:
        break

if x == -1 and y ==-1:
    print("Nao encontrado")
else:
    print(x)
    print(y)