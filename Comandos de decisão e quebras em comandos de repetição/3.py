x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

resultado = 0

if(x1 % 2 == 0):
    resultado += x1
if(x2 % 2 == 0):
    resultado += x2
if(x3 % 2 == 0):    
    resultado += x3
if(x4 % 2 == 0):
    resultado += x4
print(resultado)