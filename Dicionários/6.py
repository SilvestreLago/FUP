def funcao(vet1, vet2):
    dic = {'x': vet1[0] + vet2[0], 'y': vet1[1] + vet2[1], 'z': vet1[2] + vet2[2]}
    return dic

vet1 = []
vet2 = []
for c in range(3):
    vet1.append(float(input()))
for i in range(3):
    vet2.append(float(input()))

print(funcao(vet1, vet2))
