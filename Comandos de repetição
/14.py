def funcao(x):
    valor = 0
    z = 1
    for c in range(x):
        y = 1/z
        z += 1
        valor += y
    return valor