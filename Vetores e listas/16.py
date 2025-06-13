def funcao(x):
    vetor = []
    
    for c in range(len(x)):
        atual = x[c]
        cont = 0
        for i in range(len(x)):
            if x[i] == atual:
                cont += 1

        if cont == 1:
            vetor.append(atual)
    
    return vetor
