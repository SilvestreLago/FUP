matriz = []
maior = 0
for c in range(4):
    lista = []
    for i in range(4):
        add = int(input())
        lista.append(add)
    matriz.append(lista)

for j in range(4):
    for k in range(4):
        listaMatriz = matriz[j]
        valor = listaMatriz[k]
        if valor > 10:
            maior += 1

print(maior)