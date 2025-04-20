def funcao(x):
    fat = 1
    for i in range(1, x + 1):
        fat *= i

    soma = 0
    while fat:
        soma += fat % 10
        fat //= 10

    return soma