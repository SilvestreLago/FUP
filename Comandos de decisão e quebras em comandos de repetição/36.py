def funcao(x):
    fator = 2
    maior = 1

    while fator * fator <= x:
        if x % fator == 0:
            x = x // fator
            maior = fator
        else:
            fator = fator + 1

    if x > maior:
        maior = x

    return maior

print(funcao(5))