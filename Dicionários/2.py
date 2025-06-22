lista = []
economico = {'modelo': '', 'consumo': 0}

for c in range(5):
    carro = {}
    modelo = input()
    consumo = float(input())
    carro['modelo'] = modelo
    carro['consumo'] = consumo
    carro['distancia'] = consumo * 50
    carro['litros'] = 1000 / consumo
    lista.append(carro)

for i in range(5):
    modelo = lista[i]['modelo']
    consumo = lista[i]['consumo']
    if consumo > economico['consumo']:
        economico.update({'modelo': modelo, 'consumo': consumo})

print(f"Carro mais economico: {economico['modelo']}")

for j in range(5):
    print(f"Carro {lista[j]['modelo']} percorre {lista[j]['distancia']:.2f} kms com 50 litros")

for q  in range(5):
    print(f"Carro {lista[q]['modelo']} precisa de {lista[q]['litros']:.2f} litros para percorrer 1000 kms")
