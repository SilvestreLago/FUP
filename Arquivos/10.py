arq_entrada = input()
arq_saida = input()
cidades = []

maior_populacao = -1
cidade_mais_populosa_nome = ""
cidade_mais_populosa_habitantes = 0

with open(arq_entrada, 'r') as entrada:
    for linha_completa in entrada:
        linha_sem_quebra = linha_completa[:-1]

        info = linha_sem_quebra.split('\t')

        nome_cidade = info[0]
        habitantes = int(info[1])

        dicionario_cidade = {}
        dicionario_cidade['nome'] = nome_cidade
        dicionario_cidade['habitantes'] = habitantes
        cidades.append(dicionario_cidade)

        if habitantes > maior_populacao:
            maior_populacao = habitantes
            cidade_mais_populosa_nome = nome_cidade
            cidade_mais_populosa_habitantes = habitantes

with open(arq_saida, 'w') as saida:
    saida.write(cidade_mais_populosa_nome + '\t' + str(cidade_mais_populosa_habitantes) + '\n')

for cidade_atual in cidades:
    print(cidade_atual)

with open(arq_saida, 'r') as saida_para_leitura:
    conteudo_saida_linha = saida_para_leitura.readline()
    print(conteudo_saida_linha[:-1])