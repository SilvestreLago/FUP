def funcao(x1, x2):
    tam1 = len(x1)
    tam2 = len(x2)

    if tam1 != tam2:
        return False
    
    for c in range(tam1):
        if x1[c] != x2[c]:
            return False
        
    return True

print(funcao('teste', 'teste'))