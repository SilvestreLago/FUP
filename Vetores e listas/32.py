segue = "S"
cont = 0
alunos = []

while segue == "S" and cont < 5:
    cont += 1
    aluno = input("Aluno: ")
    alunos.append(aluno)
    if cont != 5:
        segue = input("Deseja inserir novo aluno? [S/N] ")

pesquisa = input("Aluno para pesquisa: ")

for c in range(len(alunos)):
    alunoPesquisa = alunos[c]
    tamAluno = len(alunoPesquisa)
    tamPesquisa = len(pesquisa)

    for i in range(tamAluno - tamPesquisa + 1):
        igual = True
        for j in range(tamPesquisa):
            if alunoPesquisa[i + j] != pesquisa[j]:
                igual = False
                break
        if igual:
            print(alunoPesquisa)
            print(c)
            break
