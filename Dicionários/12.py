alunos = []
aprovados = []
reprovados = []

for c in range(10):
    aluno = {}
    aluno['nome'] = input()
    aluno['matricula'] = int(input())
    aluno['media'] = float(input())
    alunos.append(aluno)

for i in range(10):
    if alunos[i]['media'] >= 5:
        aprovados.append(alunos[i])
    else:
        reprovados.append(alunos[i])

for j in range(len(aprovados)):
    print(aprovados[j])
for k in range(len(reprovados)):
    print(reprovados[k])