vetor = []
num = 0
while len(vetor) < 100:
    num += 1
    if not(num % 7 == 0) and num % 10 != 7:
        vetor.append(num)
print(vetor)