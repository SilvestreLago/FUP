def funcao(arquivo, nome):
    arq = open(arquivo, 'r')
    content = arq.read().lower()
    cont = 0
    palavra = ''
    for conteudo in content:
        if conteudo != ' ' and conteudo != '\n':
            palavra += conteudo
            if palavra == nome.lower():
                cont +=1
                palavra = ''
        else:
            if palavra == nome.lower():
                cont +=1
            palavra = ''
    return cont

x1 = input("")
x2 = input("")
y = funcao(x1, x2)
print(f"{y}")