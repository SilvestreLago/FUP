def funcao(x):
    f1 = 1
    f2 = 1
    for c in range(x-2):
        soma = f1 + f2
        f1 = f2
        f2 = soma
    return f2