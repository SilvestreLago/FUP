def funcao(x1, x2):
    if x1 <= 0 or x2 <= 0:
        return 0

    while x1 != x2:
        if x1 > x2:
            x1 = x1 - x2
        else:
            x2 = x2 - x1
    return x1

print(funcao(2, 1))