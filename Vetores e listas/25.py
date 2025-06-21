def funcao(x1, x2):
    vetor = []
    for c in range(5):
        existe = False
        for k in range(len(vetor)):
            if vetor[k] == x1[c]:
                existe = True
                break
        if not existe:
            vetor.append(x1[c])
    for c in range(5):
        existe = False
        for k in range(len(vetor)):
            if vetor[k] == x2[c]:
                existe = True
                break
        if not existe:
            vetor.append(x2[c])
    return vetor