num = int(input())
resultado = "Primo"
for c in range(2, num):
    cont = num % c
    if cont == 0:
        resultado = "Nao primo"
        break
if num == 1:
    resultado = "Nao primo"
print(resultado)