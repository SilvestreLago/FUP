def simplificar(x, y):
    if x < 0:
        nume = -x
    else:
        nume = x
    if y < 0:
        deno = -y
    else:
        deno = y

    while y != 0:
        resto = x % y
        x = y
        y = resto
        mdc = x
    
    num = nume // mdc
    den = deno // mdc

    return num, den

print(simplificar(36, 60))