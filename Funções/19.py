def funcao(x):
    n100 = x // 100
    x = x % 100
    n50 = x // 50
    x = x % 50
    n20 = x // 20
    x = x % 20
    n10 = x // 10
    x = x % 10
    n5 = x // 5
    x = x % 5
    n2 = x // 2
    x = x % 2
    n1 = x // 1
    return n100, n50, n20, n10, n5, n2, n1