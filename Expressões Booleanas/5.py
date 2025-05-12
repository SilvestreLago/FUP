a = int(input())
b = int(input())
c = int(input())

if a+b > c and a+c > b and b+c > a:
    if a == b and a == c:
        txt = 'Triangulo equilatero'
    elif (a == b and b != c) or (a == c and b != c) or (b == c and a != c):
        txt = 'Triangulo isosceles'
    elif a != b and a != c and b!=c:
        txt = 'Triangulo escaleno'
else:
    txt = 'Nao triangulo'

print(txt)