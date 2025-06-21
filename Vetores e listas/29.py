def funcao(x1):
    n = len(x1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if x1[j] < x1[j + 1]:
                temp = x1[j]
                x1[j] = x1[j + 1]
                x1[j + 1] = temp
    return x1
