x = input()
tam = len(x)
cont = 0
for c in range(tam):
    if x[c] == '1':
        cont += 1
print(cont)