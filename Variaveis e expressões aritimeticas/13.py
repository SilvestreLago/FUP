num = int(input())
centena = num // 100
dezena = (num // 10) % 10
unidade = num % 10
invertido = unidade * 100 + dezena * 10 + centena
print(invertido)