for c in range(1000, 10000):
    calc = c / 100
    prim = int(calc)
    sec = int((calc - prim)*100)
    soma = prim + sec
    quad = soma ** 2
    if quad == c:
        print(c)
