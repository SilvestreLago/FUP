def inserir(lista):
    pessoa = {
    'nome': input("Nome: "),
        'email': input("E-mail: "),
        'endereco': {
            'rua': input("Rua: "),
            'numero': int(input("Numero: ")),
            'complemento': input("Complemento: "),
            'bairro': input("Bairro: "),
            'cep': input("CEP: "),
            'cidade': input("Cidade: "), 
            'estado': input("Estado: "),
            'pais': input("Pais: ")
        },
        'telefone': {'ddd': int(input("DDD: ")), 'numero': input("Telefone: ")}, 
        'nascimento': {'dia': int(input("Dia do nascimento: ")), 'mes': int(input("Mes do nascimento: ")), 'ano': int(input("Ano do nascimento: "))},
        'observacao': input("Observacao: ")
    }
    lista.append(pessoa)
    
def busca_nome(lista, busca):
    genteai = []
    for nome in lista:
        if nome['nome'].split()[0].lower().startswith(busca.lower()):
            genteai.append(nome)
    return genteai
    
def busca_mes(lista, busca):
    mesgenteai = []
    for nome in lista:
        if nome['nascimento']['mes'] == busca:
            mesgenteai.append(nome)
    return mesgenteai

def busca_mes_dia(lista, busca1, busca2):
    mesdiagenteai = []
    for nome in lista:
        if nome['nascimento']['dia'] == busca1 and nome['nascimento']['mes'] == busca2:
            mesdiagenteai.append(nome)
    return mesdiagenteai

def agenda_listada(lista, opcao):
    if opcao == 1:
        for pessoa in lista:
            resumo = {
            'nome': pessoa['nome'],
            'telefone': pessoa['telefone'],
            'email': pessoa['email']
            }
            print(resumo)
    elif opcao == 2:
        for pessoa in lista:
            print(pessoa)
    else:
        print("Opcao invalida")

agenda = []

while True:
    print("1: Inserir uma pessoa")
    print("2: Buscar por primeiro nome")
    print("3: Buscar por mes de nascimento")
    print("4: Buscar por dia e mes de nascimento")
    print("5: Imprimir agenda")
    print("0: Sair")
    i = int(input("Opcao: "))
    if i == 0:
        break
    elif i == 1:
        inserir(agenda)
    elif i == 2:
        povo = busca_nome(agenda, input("Primeiro nome: "))
        for gente in povo:
            print(gente)
    elif i == 3:
        mespovo = busca_mes(agenda, int(input("Mes de nascimento: ")))
        for gente in mespovo:
            print(gente)
    elif i == 4:
        mesdiapovo = busca_mes_dia(agenda, int(input("Dia do nascimento: ")), int(input("Mes do nascimento: ")))
        for gente in mesdiapovo:
            print(gente)
    elif i == 5:
        print("1: Imprimir apenas nome, telefone e email")
        print("2: Imprimir todos os dados")
        agenda_listada(agenda, int(input("Opcao: ")))
    else:
        print("Opcao invalida")