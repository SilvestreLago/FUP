x = input()

tamanho = 0

for c in x:
    tamanho += 1

for c in range(tamanho):
    print(x[tamanho - 1 - c], end='')