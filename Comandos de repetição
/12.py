def funcao(x1, x2):
    y = x1 - x2
    
    k = 1
    for v in range(1, x2 + 1):
        k *= v
    
    z = 1
    for b in range(1, y + 1):
        z *= b
    
    w = k * z 
    
    n = 1
    for c in range(1, x1 + 1):
        n *= c

    resultado = n / w

    return resultado