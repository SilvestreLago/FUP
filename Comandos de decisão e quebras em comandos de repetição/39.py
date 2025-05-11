def funcao(x1, x2):
    tam1 = len(x1)
    tam2 = len(x2)
    menor = x1
    
    if tam1 > tam2:
        tam1 = tam2
        menor = x2

    for c in range(tam1):
        if x1[c] > x2[c]:
            return x2
        elif x1[c] < x2[c]:
            return x1
    return menor
        
x1 = input()
x2 = input()

print(funcao(x1, x2))