import math

n = int(input())

for c in range(n): 
    for v in range(c + 1):
        result = math.factorial(c) // (math.factorial(v) * math.factorial(c - v))
        print(result, end= ' ')
    print('')