v1 = float(input())
operador = input()
v2 = float(input())

if operador == "+":
    resultado = v1 + v2
elif operador == "-":
    resultado = v1 - v2
elif operador == "*":
    resultado = v1 * v2
elif operador == "/":
    if v2 == 0:
        resultado = "Erro"
    else:
        resultado = v1 / v2

print(f"{resultado:.2f}")