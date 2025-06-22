carros = []
for c  in range(5):
    carro = {}
    carro['modelo'] = input()
    carro['ano'] = int(input())
    carro['preco'] = float(input())
    carros.append(carro)

p = int(input())
while p != 0:
    for i in range(5):
        if carros[i]['preco'] < p:
            print(carros[i])
    p = int(input())

        