lista = []
quant = int(input())
for c in range(quant):
    alunos = {}
    alunos['matricula'] = int(input())
    alunos['nome'] = input()
    alunos['codigo'] = input()
    alunos['nota1'] = float(input())
    alunos['nota2'] = float(input())
    alunos['media'] = (alunos['nota1'] + (alunos['nota2'] * 2)) / 3
    lista.append(alunos)

for i in range(quant):
    print(lista[i])