lista = []
soma = 0

for c in range(15):
    num = float(input())
    lista.append(num)
    soma += num

media = soma / len(lista)
print(f"{media:.2f}")