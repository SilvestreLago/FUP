def contem(parte, texto):
    for i in range(len(parte) - len(texto) + 1):
        igual = True
        for j in range(len(texto)):
            if parte[i + j].lower() != texto[j].lower():
                igual = False
                break
        if igual:
            return True
    return False

livros = []

for i in range(5):
    livros.append({'titulo': input(), 'autor': input(), 'ano': int(input())})

search = input()

for livro in livros:
    if contem(livro['titulo'], search):
        print(livro)