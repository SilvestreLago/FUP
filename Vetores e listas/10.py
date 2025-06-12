lista = []

for c in range(20):
    num = int(input())
    if(num>0):
        lista.append(num)
    else:
        lista.append(0)

for c in range(20):
    print(lista[c])
