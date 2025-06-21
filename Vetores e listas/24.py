def funcao(x1, x2):
    vetor = []
    for c in range(5):
        for i in range(5):
            if x1[c] == x2[i]:
                existe = False
                for k in range(len(vetor)):
                    if vetor[k] == x1[c]:
                        existe = True
                        break
                if not existe:
                    vetor.append(x1[c])
    return vetor
