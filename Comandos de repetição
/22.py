x = int(input())
cont = 1
for c in range(1, x+1):
    for v in range(c):
        print(cont, end=" ")
        cont +=1
    print()