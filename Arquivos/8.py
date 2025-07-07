arquivo = open(input(), 'r')
arquivo2 = open(input(), 'w')
for linha in arquivo:
    print(linha, end='')
arquivo.seek(0)
for linha2 in arquivo:
    print(linha2.upper(), end='')
    arquivo2.write(linha2.upper())