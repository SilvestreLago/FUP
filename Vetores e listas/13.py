def funcao(x):
    media = 0
    quant = 0
    for c in range(15):
        if x[c] < 7:
            quant += 1
        media += x[c]
    media = media / 15

    quad = 0
    for i in range(15):
        diferenca = x[i] - media
        quad = quad + (diferenca * diferenca)

    desvio = (quad / 15) ** 0.5

    return media, desvio, quant