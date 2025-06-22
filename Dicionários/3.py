lista = []
quant = int(input())

for c in range(quant):
    alunos = {}
    alunos['nome'] = input()
    alunos['matricula'] = int(input())
    alunos['curso'] = input()
    lista.append(alunos)

for i in range(quant):
    print(lista[i])