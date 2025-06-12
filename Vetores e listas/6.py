lista = []

for c in range(8):
    num = float(input())
    lista.append(num)

x = int(input())
y = int(input())

soma = lista[x] + lista[y]

print(f"{soma:.2f}")
