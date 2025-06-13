import random

def funcao(x):
    random.seed(x)
    vetor = []
    
    for c in range(12):
        numero = random.uniform(-10, 10)
        vetor.append(numero)

    negativos = 0
    positivos = 0

    for i in range(12):
        if vetor[i] < 0:
            negativos = negativos + 1
        else:
            positivos = positivos + vetor[i]

    return negativos, positivos

seed = int(input())
x, y = funcao(seed)
print(x)
print(f"{y:.2f}")