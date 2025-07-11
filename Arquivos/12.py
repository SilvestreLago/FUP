nome = input()
arq = open(nome, "r", encoding="utf-8")
caracteres = 0
linhas = 0
palavras = 0
repeticao = {}
letra = 'a'
while letra <= 'z':
    repeticao[letra] = 0
    letra = chr(ord(letra) + 1)
linha = arq.readline()
while linha != "":
    linhas += 1
    caracteres += len(linha)
    li_palavras = linha.strip().split()
    palavras += len(li_palavras)
    for letra in linha:
        if letra.isalpha():
            letra_min = letra.lower()
            if letra_min >= 'a' and letra_min <= 'z':
                repeticao[letra_min] += 1
    linha = arq.readline()
arq.close()
print(caracteres)
print(linhas)
print(palavras)
letra = 'a'
while letra <= 'z':
    print(letra + ":", repeticao[letra])
    letra = chr(ord(letra) + 1)