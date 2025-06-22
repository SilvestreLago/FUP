matrizOriginal = []
matrizAlterada = []

for c in range(12):
    listaOriginal = []
    for i in range(13):
        listaOriginal.append(float(input()))
    matrizOriginal.append(listaOriginal)

for j in range(12):
    maior = 0
    listaAlterada = []
    for k in range(13):
        num = matrizOriginal[j][k]
        if num < 0:
            num *= -1
        if num > maior:
            maior = num
    
    for l in range(13):
        num2 = matrizOriginal[j][l]
        val = num2 / maior
        listaAlterada.append(val)
    matrizAlterada.append(listaAlterada)

for x in range(12):
    for y in range(13):
        print(f"{matrizOriginal[x][y]:.2f}", end=" ")
    print('')

print('')

for g in range(12):
    for h in range(13):
        print(f"{matrizAlterada[g][h]:.2f}", end=" ")
    print('')