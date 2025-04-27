num1 = int(input())
num2 = int(input())
if num1 > num2:
    num1, num2 = num2, num1
soma = 0
mult = 1
for c in range(num1, num2+1):
    if c % 2 == 0:
        soma += c
    else:
        mult *= c
print(soma)
print(mult)