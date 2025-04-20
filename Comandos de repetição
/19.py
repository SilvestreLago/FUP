def funcao(x):
    cont = 1
    for c in range(x):
        for v in range(cont):
            print("!", end="")
        print()
        cont += 1

funcao(10)