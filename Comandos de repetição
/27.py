def funcao(x):
    result = 1
    for c in range(x+1):
        result = c**result
    return result

print(funcao(4))