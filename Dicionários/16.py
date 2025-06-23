lista = []

for c in range(5):
    compromisso = {}
    data = {}
    compromisso['compromisso'] = input('Descricao: ')
    data['dia'] = int(input('Dia: '))
    data['mes'] = int(input('Mes: '))
    data['ano'] = int(input('Ano: '))
    compromisso['data'] = data
    lista.append(compromisso)

m = int(input())
if (m == 0):
    quit()
a = int(input())
while m != 0:
    for j in range(5):
        if (lista[j]['data']['mes'] == m and lista[j]['data']['ano'] == a):
            print(lista[j])
    m = int(input())
    if (m == 0):
        quit()
    a = int(input())