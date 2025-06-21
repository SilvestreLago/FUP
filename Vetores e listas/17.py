def funcao(vetor, num):
    valor = []
    for c in range(len(vetor)):
        if vetor[c] % num == 0:
            valor.append(vetor[c])
    return valor