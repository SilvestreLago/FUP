def funcao(x):
    cont = 1
    for c in range(x):
        y = x - cont
        for v in range(y):
            print(" ", end="")
        for b in range(2 * cont - 1):
            print("*", end="")
        print("")
        cont += 1
funcao(10)
