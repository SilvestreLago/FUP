def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)

def sf(x):
    if x == 0:
        return 1  
    elif x == 1:
        return 1
    else:
        return fatorial(x) * sf(x - 1)
