a = int(input())
b = int(input())
c = int(input())

if a>b>c:
    maior = a
    meio = b
    menor = c
elif a>c>b:
    maior = a
    meio = c
    menor = b

elif b>a>c:
    maior = b
    meio = a
    menor = c
elif b>c>a:
    maior = b
    meio = c
    menor = a

elif c>a>b:
    maior = c
    meio = a
    menor = b
elif c>b>a:
    maior = c
    meio = b
    menor = a

elif a == b == c:
    maior = a
    meio = b
    menor = c

elif a == b > c:
    maior = a
    meio = b
    menor = c
elif a == b < c:
    maior = c
    meio = a
    menor = b

elif a == c > b:
    maior = a
    meio = c
    menor = b
elif a == c < b:
    maior = b
    meio = a
    menor = c

elif b == c > a:
    maior = b
    meio = c
    menor = a
elif b == c < a:
    maior = a
    meio = b
    menor = c

elif b == a > c:
    maior = b
    meio = a
    menor = c
elif b == a < c:
    maior = c
    meio = b
    menor = a

elif c == a > b:
    maior = c
    meio = a
    menor = b
elif c == a < b:
    maior = b
    meio = c
    menor = a

elif c == b > a:
    maior = c
    meio = b
    menor = a
elif c == b < a:
    maior = a
    meio = c
    menor = b

print(menor)
print(meio)
print(maior)