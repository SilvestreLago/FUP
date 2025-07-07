arquivo = open('arq.txt', 'w')
while True:
    linha = input()
    if linha == '0':
        break
    arquivo.write(linha + '\n')
arquivo.close()

arquivo2 = open('arq.txt', 'r')
for linha2 in arquivo2:
    print(linha2, end='')
arquivo2.close()