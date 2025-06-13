vetor = []
rep =[]

for c in range(10):
    vetor.append(int(input()))

for i in range(len(vetor)):
    for v in range(i+1, len(vetor)):
        if vetor[i] == vetor[v]:
            rep.append(vetor[i])

for j in range(len(rep)):
    print(rep[j])