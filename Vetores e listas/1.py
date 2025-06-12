def funcao(data):
    dia = data[0:2]
    if(dia[0] == "0"):
        dia = data[1]
    mes = int(data[3:5])
    ano = data[6:10]
    

    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    extenso = f"{dia} de {meses[mes - 1]} de {ano}"
    return extenso

print(funcao("05/03/1997"))