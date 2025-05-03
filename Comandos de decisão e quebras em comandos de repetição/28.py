num = int(input())
for c in range(1, num+1):
    cont = num % c
    if cont == 0:
        print(c)