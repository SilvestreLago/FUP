x = input()

tam = len(x)
txt = ''
txtI = ''
cont = 0

for c in range(tam-1, -1, -1):
    if ord(x[c]) >= 65:
        if ord(x[c]) <= 90:
            txtI += x[c]
    if ord(x[c]) >=97:
        if ord(x[c]) <= 122:
            letra= chr(ord(x[c])-32)
            txtI += letra
for c in range(tam):
    if ord(x[c]) >= 65:
        if ord(x[c]) <= 90:
            txt += x[c]
    if ord(x[c]) >=97:
        if ord(x[c]) <= 122:
            letra= chr(ord(x[c])-32)
            txt += letra

tam2 = len(txt)

for c in range(tam2):
    if txtI[c] != txt[c]:
        print(False)
        exit()

print(True)