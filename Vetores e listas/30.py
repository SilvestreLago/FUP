def funcao(vetor):
    n = len(vetor)
    tam = 0
    pos1 = pos2 = -1
    for i in range(n):
        for j in range(i + 1, n):
            k = 0
            while i + k < n and j + k < n and vetor[i + k] == vetor[j + k]:
                k += 1
            if k >= 2 and k > tam:
                tam = k
                pos1 = i
                pos2 = j
    if tam >= 2:
        return pos1, pos2, tam
    else:
        return -1, -1, -1