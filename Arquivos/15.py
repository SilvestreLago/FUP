nome_arquivo_entrada = input()
dia_hoje = int(input())
mes_hoje = int(input())
ano_hoje = int(input())

nome_arquivo_saida = nome_arquivo_entrada + ".out"

resultados = []

with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
    for linha in arquivo_entrada:
        if not linha.strip():
            continue

        partes_linha = linha.strip().split('\t', 1)
        nome = partes_linha[0]
        data_str = partes_linha[1]

        partes_data = data_str.split()

        dia_nasc = int(partes_data[0])
        mes_nasc = int(partes_data[1])
        ano_nasc = int(partes_data[2])

        idade = ano_hoje - ano_nasc

        if mes_hoje < mes_nasc:
            idade -= 1
        elif mes_hoje == mes_nasc:
            if dia_hoje < dia_nasc:
                idade -= 1

        status_maioridade = ""
        if idade < 18:
            status_maioridade = "menor de idade"
        elif idade > 18:
            status_maioridade = "maior de idade"
        else:
            status_maioridade = "entrando na maioridade"

        resultados.append(f"{nome}\t{idade}\t{status_maioridade}")

with open(nome_arquivo_saida, 'w') as arquivo_saida:
    arquivo_saida.write("\n".join(resultados))

with open(nome_arquivo_saida, 'r') as arquivo_para_leitura:
    print(arquivo_para_leitura.read())