letras = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
    'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
    'z': 0
}
carac = 0
palavra = 0
linha = 0

arquivo = open(input(), "r")

conteudo = arquivo.read()
arquivo.close()

carac = len(conteudo)


for letra in conteudo:
    if letra == '\n':
        linha +=1
if len(conteudo) > 0 and (len(conteudo) == 0 or conteudo[-1] != '\n'):
    linha += 1

separadores = [' ', '\n', '\t']
palavra_atual = ''
for c in conteudo:
    if c not in separadores:
        palavra_atual += c
    else:
        if palavra_atual != '':
            palavra += 1
            palavra_atual = ''
if palavra_atual != '':
    palavra += 1

for c in conteudo:
    c_min = c.lower()
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        letras[c_min] += 1
        
print(carac)
print(palavra)
print(linha)
for letraDic in letras:
    print(f"{letraDic}: {letras[letraDic]}")
