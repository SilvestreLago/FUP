matriz = []
for c in range(20):
    lista = []
    for k in range(20):
        lista.append(int(input()))
    matriz.append(lista)

max_produto = 0
linha_inicio = 0
coluna_inicio = 0
direcao = ""

for i in range(20):
    for j in range(20):

        if j <= 16:
            prod = matriz[i][j] * matriz[i][j+1] * matriz[i][j+2] * matriz[i][j+3]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "direita"

        if j >= 3:
            prod = matriz[i][j] * matriz[i][j-1] * matriz[i][j-2] * matriz[i][j-3]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "esquerda"

        if i <= 16:
            prod = matriz[i][j] * matriz[i+1][j] * matriz[i+2][j] * matriz[i+3][j]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "baixo"

        if i >= 3:
            prod = matriz[i][j] * matriz[i-1][j] * matriz[i-2][j] * matriz[i-3][j]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "cima"

        if i <= 16 and j <= 16:
            prod = matriz[i][j] * matriz[i+1][j+1] * matriz[i+2][j+2] * matriz[i+3][j+3]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "direita baixo"

        if i >= 3 and j <= 16:
            prod = matriz[i][j] * matriz[i-1][j+1] * matriz[i-2][j+2] * matriz[i-3][j+3]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "direita cima"

        if i <= 16 and j >= 3:
            prod = matriz[i][j] * matriz[i+1][j-1] * matriz[i+2][j-2] * matriz[i+3][j-3]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "esquerda baixo"

        if i >= 3 and j >= 3:
            prod = matriz[i][j] * matriz[i-1][j-1] * matriz[i-2][j-2] * matriz[i-3][j-3]
            if prod > max_produto:
                max_produto = prod
                linha_inicio = i
                coluna_inicio = j
                direcao = "esquerda cima"

print(max_produto)
print(linha_inicio)
print(coluna_inicio)
print(direcao)
