nome = input()
idade = int(input())

maiorN = nome
maiorI = idade

menorN = nome
menorI = idade

while idade >=0:
    if idade > maiorI:
        maiorN = nome
        maiorI = idade

    elif idade < menorI:
        menorN = nome
        menorI = idade

    nome = input()
    idade = int(input())

print(menorN)
print(menorI)
print(maiorN)
print(maiorI)