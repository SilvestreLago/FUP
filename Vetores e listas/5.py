lista = []
listaQuad = []

for c in range(10):
    num = float(input())
    lista.append(num)

for c in range(10):
    listaQuad.append(lista[c] ** 2)

for c in range(10):
    print(f"{lista[c]:.2f}")

for c in range(10):
    print(f"{listaQuad[c]:.2f}")