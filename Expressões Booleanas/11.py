def funcao(x):
    if len(x) != 10:
        return 0, 0, 0
    
    dia = x[0] + x[1]
    mes = x[3] + x[4]
    ano = x[6] + x[7] + x[8] + x[9]

    cont = 0
    while cont < 2:
        if not(dia[cont] >= '0' and dia[cont] <= '9'):
            return 0, 0, 0
        if not(mes[cont] >= '0' and mes[cont] <= '9'):
            return 0, 0, 0
        cont += 1
    
    cont = 0
    while cont < 4:
        if not(ano[cont] >= '0' and ano[cont] <= '9'):
            return 0, 0, 0
        cont += 1

    if dia[0] == '0':
        dia = dia[1]
    if mes[0] == '0':
        mes = mes[1]

    return dia, mes, ano

dia, mes, ano = funcao('02/09/2004')

print(dia)
print(mes)
print(ano)