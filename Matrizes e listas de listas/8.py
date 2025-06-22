matriz = []
soma = 0
dp = 0
for c in range(4):
    lista = []
    for i in range(4):
        lista.append(int(input()))
    matriz.append(lista)

for j in range(4):
    for k in range(4):
        if k > dp:
            soma += matriz[j][k]
    dp += 1

print(soma)