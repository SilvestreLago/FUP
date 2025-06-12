lista = []
soma = 0

for c in range(15):
    num = int(input())
    if(num % 2 != 0):
        lista.append(num)
        soma += num

print(soma)
for c in range(len(lista)):
    print(lista[c])