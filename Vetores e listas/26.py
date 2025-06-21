def funcao(x1, x2):
    vetor = []
    for i in range(len(x1)):
        existe = False
        for j in range(len(x2)):
            if x1[i] == x2[j]:
                existe = True
                break
        if not existe:
            adicionado = False
            for k in range(len(vetor)):
                if vetor[k] == x1[i]:
                    adicionado = True
                    break
            if not adicionado:
                vetor.append(x1[i])
    return vetor