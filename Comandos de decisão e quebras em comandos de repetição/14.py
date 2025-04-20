def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

menu = "1 - Adicao\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao\n5 - Saida"
print(menu)

opcao = int(input())

while opcao != 5:
    a = float(input())
    b = float(input())
    if(opcao == 1):
        print(f"{soma(a, b):.2f}")
    elif(opcao == 2):
        print(f"{subtracao(a, b):.2f}")
    elif(opcao == 3):
        print(f"{multiplicacao(a, b):.2f}")
    elif(opcao == 4):
        print(f"{divisao(a, b):.2f}")
    print(menu)
    opcao = int(input())