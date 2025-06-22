import random
matriz = []

x = int(input())
y = int(input())
random.seed(int(input()))
intervaloInicio = int(input())
intervaloFim = int(input())

for c in range(x):
    lista = []
    for i in range(y):
        lista.append(random.randint(intervaloInicio, intervaloFim))
    matriz.append(lista)

for z in range(x):
    for e in range(y):
        print(matriz[z][e], end=" ")
    print('')

for j in range(x):
    if j%2 == 0:
        soma = 0
        for q in range(y):
            soma += matriz[j][q]
        print(f"{soma / y:.2f}")
    elif j%2 == 1:
        quant = 0
        for w in range(y):
            val = matriz[j][w]
            if val < 0 and val % 3 == 0:
                quant += 1
        print(quant)