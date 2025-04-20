n1 = 1
n2 = 0
for c in range(9):
    for v in range(10):
        result = n1 + n2
        print(f"{n1} + {n2} = {result}")
        n2 +=1
    n2 = 0
    n1 += 1