def funcao(x):
    y = x**(1/2)
    z = y*y
    if z == x:
        return True
    else:
        return False
print(funcao(0))