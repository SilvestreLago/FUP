num = float(input())
maior = num
menor = num
for c in range(9):
    num = float(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f"{menor:.2f}")
print(f"{maior:.2f}")