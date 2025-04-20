a = float(input())
b = float(input())
c = float(input())
delta = b ** 2 - 4 * a * c
if a == 0:
    print("Nao eh equacao do 2o grau")
    exit()
if delta < 0:
    print("Nao existe raiz real")
    exit()
elif delta == 0:
    x1 = (-b + delta ** 0.5) / (2 * a)
    print(f"{x1:.2f}")
    print("Raiz unica")
    exit()
elif delta > 0:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"{x1:.2f}")
    print(f"{x2:.2f}")
