def funcao(x1, x2, x3, x4):
    
    peso1 = 1
    peso2 = 1
    peso3 = 1

    if x4 == "P":
        peso1 = 5
        peso2 = 3
        peso3 = 2
    
    nota = ((x1 * peso1) + (x2 * peso2) + (x3 * peso3)) / (peso1 + peso2 + peso3)
    return nota
