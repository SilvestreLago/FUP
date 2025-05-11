num = int(input())
soma = 0
for c in range(1, num):
    perf = num % c
    if perf == 0:
        soma += c
if soma == num:
    print('Perfeito')
else:
    print('Nao perfeito')