produtos = []

for i in range(5):
    coisa = {
        'codigo':int(input()),
        'nome':input(),
        'preco':float(input()),
        'quantidade':int(input())}
    produtos.append(coisa)

codigo_procura = -1

while True:
    for coisa in produtos:
        print(coisa)

    codigo_procura = int(input())
    if codigo_procura == 0:
        break
    quantia = int(input())

    tem = False
    for coisa in produtos:
        if codigo_procura == coisa['codigo']:
            tem = True
            if quantia > coisa['quantidade']:
                print("Impossivel atender ao pedido, produto sem estoque suficiente")
            else:
                coisa['quantidade'] -= quantia
            break
        
    if not tem:
        print("Impossivel atender ao pedido, codigo nao encontrado")