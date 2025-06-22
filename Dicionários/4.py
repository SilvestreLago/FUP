lista = []
quant = int(input())

for c in range(quant):
    compromisso = {}
    compromisso['dia'] = int(input())
    compromisso['mes'] = int(input())
    compromisso['ano'] = int(input())
    compromisso['hora'] = int(input())
    compromisso['minuto'] = int(input())
    compromisso['segundo'] = int(input())
    compromisso['descricao'] = input()

for i in range(quant):
    print(quant)
    print(f"Dia: {compromisso['dia']}")
    print(f"Mes: {compromisso['mes']}")
    print(f"Ano: {compromisso['ano']}")
    print(f"Hora: {compromisso['hora']}")
    print(f"Minuto: {compromisso['minuto']}")
    print(f"Segundo: {compromisso['segundo']}")
    print(f"Descricao: {compromisso['descricao']}")

