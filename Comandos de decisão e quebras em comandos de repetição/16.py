num = int(input())
if num < 0:
    exit()
else:
    maior = num
    menor = num
    while num > 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        num = int(input())
print(maior)
print(menor)