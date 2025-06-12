lista = []

for c in range(15):
    num = int(input())
    if(num % 2 == 0):
        lista.append(num)

print(len(lista))
for c in range(len(lista)):
    print(lista[c])