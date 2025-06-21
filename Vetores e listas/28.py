vetor = []
while True:
    if len(vetor) == 12:
        break
    num = int(input())
    repetido = False
    for c in range(len(vetor)):
        if num == vetor[c]:
            print(f"Numero {num} ja existe, escreva outro")
            repetido = True
            break 
    if repetido:
        continue
    vetor.append(num)
print(vetor)
