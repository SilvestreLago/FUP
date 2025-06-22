    lista = []

    for c in range(5):
        compromisso = {}
        compromisso['descricao'] = input()
        compromisso['dia'] = int(input())
        compromisso['mes'] = int(input())
        compromisso['ano'] = int(input())
        lista.append(compromisso)

    for i in range(5):
        print(f"Descricao: {lista[i]['descricao']}")
        print(f"Dia: {lista[i]['dia']}")
        print(f"Mes: {lista[i]['mes']}")
        print(f"Ano: {lista[i]['ano']}")

    m = int(input())
    if (m == 0):
        quit()
    a = int(input())
    while m != 0:
        for j in range(5):
            if (lista[j]['mes'] == m and lista[j]['ano'] == a):
                print(lista[j])
        m = int(input())
        if (m == 0):
            quit()
        a = int(input())