num = int(input())
cont = 0
for c in range(1, num):
    if num % c == 0:
        cont += c
print(cont)