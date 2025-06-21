vetor = []
for c in range(100):
    vetor.append(float(input()))

while True:
    valor = int(input())
    if valor == 0:
        break
    elif valor == 1:
        for c in range(100):
            print(vetor[c])
    elif valor == 2:
        reverseVetor = []
        cont = 100
        for c in range(101):
            reverseVetor.append(vetor[cont-1])
            cont -= 1
        for c in range(100):
            print(reverseVetor[c])
    else:
        print("Codigo invalido")
