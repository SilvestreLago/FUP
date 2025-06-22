import random
matriz = []
matrizAlterada = []
dp = 0

random.seed(int(input()))

for c in range(5):
    lista = []
    for i in range(5):
        lista.append(random.randint(1, 20))
    matriz.append(lista)
    matrizAlterada.append(lista.copy())

for j in range(5):
    for k in range(5):
        while k > dp:
            matrizAlterada[j][k] = 0
            break
    dp += 1

for q in range(5):
    for w in range(5):
        print(matriz[q][w], end=" ")
    print('')

print('')

for x in range(5):
    for y in range(5):
        print(matrizAlterada[x][y], end=" ")
    print('')