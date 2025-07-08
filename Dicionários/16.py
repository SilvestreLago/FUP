def comparar_aulas(aula1, aula2):
    d1 = aula1['data']
    d2 = aula2['data']

    if d1['ano'] != d2['ano']:
        return d1['ano'] < d2['ano']
    if d1['mes'] != d2['mes']:
        return d1['mes'] < d2['mes']
    if d1['dia'] != d2['dia']:
        return d1['dia'] < d2['dia']

def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if comparar_aulas(lista[j], lista[menor]):
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
    return lista

compromissos = []

for i in range(5):
    compromissos.append({
    'compromisso': input("Descricao: "), 
    'data': {
        'dia':int(input("Dia: ")),
        'mes':int(input("Mes: ")) ,
        'ano': int(input("Ano: "))}
    })
    
while True:
    M = int(input())
    if M == 0:
        break
    A = int(input())
    encontrados = []
    for compromisso in compromissos:
        data = compromisso['data']
        if data['mes'] == M and data['ano'] == A:
            encontrados.append(compromisso)

    lista = ordenar_lista(encontrados)
    for coisa in lista:
        print(coisa)