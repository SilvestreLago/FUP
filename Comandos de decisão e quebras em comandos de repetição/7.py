sal = float(input())
emp = float(input())

porcento = sal * 20 / 100
if(emp > porcento):
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")