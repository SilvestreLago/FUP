def funcao(x, y):
    if y == 0:
        return 1
    else:
        return x * funcao(x, y - 1)

print(funcao(10))
