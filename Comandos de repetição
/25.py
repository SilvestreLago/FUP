def funcao(x):
    soma = 0
    for c in range(1, x + 1):
        num = c * c + 1
        den = c + 3
        soma += num / den
    soma = f"{soma:.2f}"
    return soma

print(funcao(3))