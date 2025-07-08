def comparar_aulas(aula1, aula2):
    d1, h1 = aula1['data'], aula1['horario']
    d2, h2 = aula2['data'], aula2['horario']

    if d1['ano'] != d2['ano']:
        return d1['ano'] < d2['ano']
    if d1['mes'] != d2['mes']:
        return d1['mes'] < d2['mes']
    if d1['dia'] != d2['dia']:
        return d1['dia'] < d2['dia']
    if h1['hora'] != h2['hora']:
        return h1['hora'] < h2['hora']
    if h1['minuto'] != h2['minuto']:
        return h1['minuto'] < h2['minuto']
    return h1['segundo'] < h2['segundo']

def ordenar_aulas(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if comparar_aulas(lista[j], lista[menor]):
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
    return lista

aulas = []
x = int(input())
for i in range(x):
    aula = {
        'data': {
            'dia': int(input("Dia: ")),
            'mes': int(input("Mes: ")),
            'ano': int(input("Ano: "))
        },
        'horario': {
            'hora': int(input("Hora: ")),
            'minuto': int(input("Minuto: ")),
            'segundo': int(input("Segundo: "))
        },
        'descricao': input("Descricao: ")
    }
    aulas.append(aula)
aulas_organizadas = ordenar_aulas(aulas)
for aula in aulas_organizadas:
    print(aula)