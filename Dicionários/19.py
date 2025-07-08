def maior_idade(lista):
    n = len(lista)
    maioridade = lista[0]
    for i in range(1,n):
        if lista[i]['idade'] > maioridade['idade']:
            maioridade = lista[i]
    return maioridade
    
def masculino(lista):
    n = len(lista)
    macho = []
    for i in range(n):
        if lista[i]['sexo'] == "Masculino":
            macho.append(lista[i])
    return macho
    
def salario_1001(lista):
    n = len(lista)
    rico = []
    for i in range(n):
        if lista[i]['salario'] > 1000:
            rico.append(lista[i])
    return rico

def identidade_perdida(lista,procura):
    for pessoa in lista:
        if procura == pessoa['identidade']:
            return pessoa
    return ""
        
pessoas = []

for _ in range(5):
    pessoa = {
        'nome': input("Nome: "),
        'endereco':{
            'rua': input("Rua: "),
            'bairro': input("Bairro: "),
            'cidade': input("Cidade: "),
            'estado': input("Estado: "),
            'cep': input("CEP: ")
        },
        'salario': float(input("Salario: ")),
        'identidade': (input("Identidade: ")),
        'cpf': input("CPF: "),
        'civil': input("Estado Civil: "),
        'telefone': input("Telefone: "),
        'idade': int(input("Idade: ")),
        'sexo': input("Sexo: ")
    }
    pessoas.append(pessoa)

print("Pessoa com maior idade:")
print(maior_idade(pessoas))

macho = masculino(pessoas)
print("Pessoas do sexo masculino:")
if len(macho) > 0:
    for pessoa in macho:
        print(pessoa)

rico = salario_1001(pessoas)
print("Pessoas com salario maior que 1000:")
if len(rico) > 0:
    for pessoa in rico:
        print(pessoa)
        
pessoa_identidade = identidade_perdida(pessoas, input("Identidade: "))
print(pessoa_identidade)