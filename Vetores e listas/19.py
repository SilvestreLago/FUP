def funcao(x1, x2):
    valor = []
    cont01 = 0
    cont02 = 0
    for c in range(10):
        if(c % 2 == 0):
            valor.append(x1[cont01])
            cont01 += 1
        else:
            valor.append(x2[cont02])
            cont02 += 1
    return valor