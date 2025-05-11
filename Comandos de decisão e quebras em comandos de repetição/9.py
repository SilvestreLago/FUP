a = int(input())
b = int(input())
c = int(input())

if a <= b:
    if a <= c:
        menor = a
        if b <= c:
            meio = b
            maior = c
        else:
            meio = c
            maior = b
    else:
        menor = c
        meio = a
        maior = b
else:
    if b <= c:
        menor = b
        if a <= c:
            meio = a
            maior = c
        else:
            meio = c
            maior = a
    else:
        menor = c
        meio = b
        maior = a

print(menor)
print(meio)
print(maior)