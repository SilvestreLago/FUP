x1 = float(input())
if(x1 > 10):
    print("Nota invalida")
    exit()
elif(x1 < 0):
    print("Nota invalida")
    exit()
x2 = float(input())
if(x2 > 10):
    print("Nota invalida")
    exit()
elif(x2 < 0):
    print("Nota invalida")
    exit()
x3 = float(input())
if(x3 > 10):
    print("Nota invalida")
    exit()
elif(x3 < 0):
    print("Nota invalida")
    exit()

print(f"{(x1+x2+x3)/3:.2f}")