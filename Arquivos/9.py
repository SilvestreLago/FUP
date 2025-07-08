arquivoN = input()
arquivo2N = input()
arquivo3N = arquivoN + arquivo2N
arquivo = open(arquivoN, 'r')
arquivo2 = open(arquivo2N, 'r')
arquivo3 = open(arquivo3N, 'w')
for linha in arquivo:
    arquivo3.write(linha)    
for linha2 in arquivo2:
    arquivo3.write(linha2)
arquivo3.close()
arquivo3 = open(arquivo3N, 'r')
for linha3 in arquivo3:
    print(linha3, end='')