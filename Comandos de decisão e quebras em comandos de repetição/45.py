def funcao(txt, hash):
    i = 0
    cifra = ""

    while i < len(txt):
        c = txt[i]
        if c != ' ':
            asc = ord(c)
            nAsc = asc + hash
            if nAsc > ord('Z'):
                nAsc -= 26
            letra = chr(nAsc)
            cifra += letra
        else:
            cifra += ' '
        i = i + 1

    return cifra