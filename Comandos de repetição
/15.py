def funcao(x):
    e = 1
    y = 1
    for c in range(1, x + 1):
        y *= c
        e += 1/y
    return e