pessoa = {
    'nome': input(),
    'endereco': input(),
    'nascimento': input(),
    'cidade': input(),
    'cep': input(),
    'email': input(),
}

data = pessoa['nascimento']
if len(data) != 10 or data[2] != '/' or data[5] != '/' or not (data[:2] + data[3:5] + data[6:]).isdigit():
    print("Data errada")
    exit()

cep = pessoa['cep']
if len(cep) != 10 or cep[2] != '.' or cep[6] != '-' or not (cep[:2] + cep[3:6] + cep[7:]).isdigit():
    print("CEP errado")
    exit()

email = pessoa['email']
arroba = email.find('@')
ponto = email.find('.', arroba)

if (arroba == -1 or ponto == -1 or email.count("@") > 1 or ponto == arroba + 1):
    print("E-mail errado")
    exit()

print(pessoa)