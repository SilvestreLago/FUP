def funcao(x, n):
    resultado = 0
    for c in range(n + 1):
        denominador = 1
        num = (-1) ** c * (x ** (2 * c + 1))
        fat = 2 * c + 1
        for v in range(1, fat + 1 ):
            denominador *= v
        termo = num / denominador
        resultado += termo
    return resultado

print(funcao(1.570796327, 6))