num1 = int(input())
num2 = int(input())
qtd = 0

if num1 < num2:
    num1, num2 = num2, num1
    
while num1 >= num2:
    num1 = num1 - num2
    qtd = qtd + 1
print(qtd) 