def funcao(x):
    centena = x // 100
    dezena = (x // 10) % 10
    unidade = x % 10
    invertido = unidade * 100 + dezena * 10 + centena
    return invertido