def funcao(nome_arquivo, palavra):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().lower()

    palavra = palavra.lower()

    contagem = 0
    len_palavra = len(palavra)

    if len_palavra == 0:
        return 0

    for i in range(len(conteudo) - len_palavra + 1):
        fatia = conteudo[i: i + len_palavra]

        if fatia == palavra:
            contagem += 1

    return contagem