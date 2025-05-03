x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

resultado = 0

cont1 = x1 % 2
cont2 = x2 % 2
cont3 = x3 % 2
cont4 = x4 % 2

if(cont1 == 0):
    resultado += x1
if(cont2 == 0):
    resultado += x2
if(cont3 == 0):    
    resultado += x3
if(cont4 == 0):
    resultado += x4
print(resultado)