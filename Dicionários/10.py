def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1,n):
            nome1 = lista[i]['nome']
            nome2 = lista[j]['nome']
            menorlen = len(nome1)
            if menorlen > len(nome2):
                menorlen = len(nome2)
            trocou = False
            for k in range(menorlen):
                if nome1[k] > nome2[k]:
                    lista[i], lista[j] = lista[j], lista[i]
                    trocou = True
                    break
                elif nome1[k] < nome2[k]:
                    trocou = True
                    break
            if not trocou and len(nome1) > len(nome2):
                lista[i], lista[j] = lista[j], lista[i]
    return lista

alunos = []

for i in range(5):
    pessoa = {
        'nome':input(),
        'endereco':input(),
        'telefone':input()
    }
    alunos.append(pessoa)
alunos_ordenado = ordenar_lista(alunos)

for aluno in alunos_ordenado:    
    print(aluno)