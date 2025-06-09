def funcao(x):
    if x == 1:
        return 1
    else:
        return x + funcao(x - 1)
    
print(funcao(10))
