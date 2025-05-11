x = input()
tam = len(x)
txtI = ""
for c in range(tam-1, -1, -1):
    letra = x[c]
    if letra == 'a':
        letra = '*'
    elif letra == 'A':
        letra = '*'
    txtI += letra

print(txtI)