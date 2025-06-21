vetor = []
for c in range(10):
    vetor.append(int(input()))

vetorFinal = []
posicao = []

for c in range(10):
    num = vetor[c]
    if num < 0:
        num = num * -1
    if num == 2:
        vetorFinal.append(vetor[c])
        posicao.append(c)
    if num == 1 or num == 0:
        pass
    elif num % 2 == 0:
        pass
    else:
        primo = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                primo = False
                break
        if primo:
            vetorFinal.append(vetor[c])
            posicao.append(c)

for c in range(len(vetorFinal)):
    print(vetorFinal[c])
    print(posicao[c])