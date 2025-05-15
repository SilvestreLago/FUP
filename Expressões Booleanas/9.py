def funcao(x1, x2):
    if x1 <= 0 or x2 <= 0:
        return 0
    
    maior = x1
    if x2 > x1:
        maior = x2

    while True:
        if maior % x1 == 0 and maior % x2 == 0:
            return maior
        maior += 1
    
print(funcao(2, 3))