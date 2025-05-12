x = input()
y = input()

tam = len(x)
txt = ''
cont = 0

for c in range(tam):
    letra = x[c]
    if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
        cont += 1
        txt += y
    else:
        txt += letra

print(cont)
print(txt)