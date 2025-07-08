eletrodomesticos = []
soma = 0

for i in range(5):
    coisa = {
        'nome':input(),
        'potencia':float(input()),
        'tempo_ativo':float(input())}
    eletrodomesticos.append(coisa)
    
dias = int(input())

for coisa in eletrodomesticos:
    coisa['gasto'] = coisa['potencia'] * coisa['tempo_ativo'] * dias
    soma += coisa['gasto']

print(f"{soma:.2f}")

for coisa in eletrodomesticos:
    print(f"{coisa['nome']}: {(coisa['gasto']/soma)*100:.2f}")