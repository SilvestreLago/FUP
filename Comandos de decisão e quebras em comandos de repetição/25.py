cont = 0
num = 0
while cont < 10:
    n = int(input())
    if n < 0:
        pass
    elif n == 0:
        pass
    else:
        num += n
        cont += 1
print(f"{num / 10:.2f}")