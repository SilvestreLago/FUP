def funcao(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

x1 = float(input())
x2 = float(input())
x3 = float(input())

num = funcao(x1, x2, x3)
print(num)
