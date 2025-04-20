def funcao(x):
    horas = x // 3600
    minutos = (x % 3600) // 60
    segundos = x % 60
    return horas, minutos, segundos