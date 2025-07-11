nome_arquivo = input()

lista_de_contatos = []

with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        if linha_limpa:
            partes = linha_limpa.split('\t')
            contato = {'nome': partes[0], 'telefone': partes[1]}
            lista_de_contatos.append(contato)

n = len(lista_de_contatos)

for i in range(n):
    for j in range(0, n - i - 1):
        if lista_de_contatos[j]['nome'] > lista_de_contatos[j + 1]['nome']:
            temp = lista_de_contatos[j]
            lista_de_contatos[j] = lista_de_contatos[j + 1]
            lista_de_contatos[j + 1] = temp

for contato in lista_de_contatos:
    print(contato)