lista = []
maiorN1 = {'aluno': '', 'nota': 0}
maiorMedia = {'aluno': '', 'nota': 0}
menorMedia = {'aluno': '', 'nota': 100}

for c in range(5):
    alunos = {}
    alunos['matricula'] = int(input())
    alunos['nome'] = input()
    alunos['nota1'] = float(input())
    alunos['nota2'] = float(input())
    alunos['nota3'] = float(input())
    alunos['media'] = (alunos['nota1'] + alunos['nota2'] + alunos['nota3']) / 3

    if(alunos['media'] >= 7):
        alunos['aprovado'] = 'aprovado'
    else:
        alunos['aprovado'] = 'reprovado'

    if alunos['nota1'] > maiorN1['nota']:
        maiorN1.update({'aluno': alunos['nome'], 'nota': alunos['nota1']})
    
    if alunos['media'] > maiorMedia['nota']:
        maiorMedia.update({'aluno': alunos['nome'], 'nota': alunos['media']})
    
    if alunos['media'] < menorMedia['nota']:
        menorMedia.update({'aluno': alunos['nome'], 'nota': alunos['media']})

    lista.append(alunos)

print(f"Aluno {maiorN1['aluno']} tem a maior nota1: {maiorN1['nota']:.2f}")
print(f"Aluno {maiorMedia['aluno']} tem a maior media: {maiorMedia['nota']:.2f}")
print(f"Aluno {menorMedia['aluno']} tem a menor media: {menorMedia['nota']:.2f}")
for j in range(5):
    print(f"Aluno {lista[j]['nome']} esta {lista[j]['aprovado']} com media {lista[j]['media']:.2f}")

