qtd = int(input())

num = float(input())
maior = num
menor = num
for c in range(qtd-1):
    num = float(input())
    if(num > maior):
        maior = num
    if(num < menor):
        menor = num
print(f"{menor:.2f}")
print(f"{maior:.2f}")