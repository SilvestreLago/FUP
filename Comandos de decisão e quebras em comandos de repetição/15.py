num = int(input())
cont = 0
for c in range(1, num):
    div = num % c
    if div == 0:
        cont += c
print(cont)