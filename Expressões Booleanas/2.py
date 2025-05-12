x = input()
tam = len(x)
txt = ''

for c in range(tam):
    letra = x[c]
    if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
        pass
    else:
        txt += letra
print(txt)