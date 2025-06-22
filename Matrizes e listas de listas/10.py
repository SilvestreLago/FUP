matriz = []
soma = 0

for c in range(16):
    valor = int(input())
    linha = c // 4
    coluna = c % 4

    if coluna == 0:
        matriz.append([])

    matriz[linha].append(valor)

    if linha == coluna:
        soma += valor

print(soma)