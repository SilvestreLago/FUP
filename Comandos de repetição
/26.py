import math
def funcao(x, n):
    resultado = 0
    for c in range(n + 1):
        num = (-1) ** c * (x ** (2 * c + 1))
        den = math.factorial(2 * c + 1)
        termo = num / den
        resultado += termo
    return resultado

print(funcao(1.570796327, 6))