x1 = float(input())
x2 = float(input())
x3 = float(input())

if(x3 == 1):
    result = f"{(x1 + x2) / 2:.2f}"
elif(x3 == 2):
    if(x1 > x2):
        result = f"{x1 - x2:.2f}"
    elif(x2 > x1):
        result = f"{x2 - x1:.2f}"
elif(x3 == 3):
    result = f"{x1 * x2:.2f}"
elif(x3 == 4):
    if(x2 == 0):
        result = "Erro"
    else:
        result = f"{x1 / x2:.2f}"
else:
    result = "Erro"
print(result)