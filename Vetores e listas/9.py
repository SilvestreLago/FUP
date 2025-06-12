lista = []
maior = 0
menor = 0

for c in range(10):
    num = int(input())
    lista.append(num)

for c in range(10):
    if(c == 0):
        menor = lista[c]
    if(lista[c] > maior):
        maior = lista[c]
    if(lista[c] < menor):
        menor = lista[c]

print(maior)
print(menor)