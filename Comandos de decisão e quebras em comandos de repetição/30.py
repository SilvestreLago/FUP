qtd = int(input())
num = int(input())
maior = num
rep = 1
for c in range(qtd-1):
    num = int(input())
    if num > maior:
        maior = num
        rep = 1
    elif num == maior:
        rep += 1
print(maior)
print(rep)