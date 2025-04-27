num = int(input())
resultado = "Primo"
for c in range(2, num):
    if num % c == 0:
        resultado = "Nao primo"
        break
if num == 1:
    resultado = "Nao primo"
print(resultado)