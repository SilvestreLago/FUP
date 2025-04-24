def funcao(x):
    dia = x[0:2]
    ano = x[6:11]
    mes = x[3:5]
    if dia[0] == "0":
        dia = dia[1:2]
    if mes == "01":
        mes = "janeiro"
    elif mes == "02":
        mes = "fevereiro"
    elif mes == "03":
        mes = "marco"
    elif mes == "04":
        mes = "abril"
    elif mes == "05":
        mes = "maio"
    elif mes == "06":   
        mes = "junho"
    elif mes == "07":
        mes = "julho"
    elif mes == "08":
        mes = "agosto"
    elif mes == "09":
        mes = "setembro"
    elif mes == "10":
        mes = "outubro"
    elif mes == "11":
        mes = "novembro"
    elif mes == "12":
        mes = "dezembro"
    y = dia + " de " + mes + " de " + ano
    return y

x1 = "01/05/2025"
print(funcao(x1))