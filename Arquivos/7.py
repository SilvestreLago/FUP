nome_arquivo = input()
with open(f'{nome_arquivo}out', 'x') as mod_archive:
    with open(nome_arquivo, 'r') as usu_arquivo:
        for c in usu_arquivo.read():
            c_minusculo = c.lower()
            if c_minusculo == 'a' or c_minusculo == 'e' or c_minusculo == 'i' or c_minusculo == 'o' or c_minusculo == 'u':
                mod_archive.write("*")
            else:
                mod_archive.write(c)
with open(f'{nome_arquivo}out', 'r') as mod_archive:
    print(mod_archive.read())