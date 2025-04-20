v1 = float(input())
v2 = float(input())
v3 = float(input())
premio = float(input())
total = v1 + v2 + v3
tot1 = (v1 * premio) / total
tot2 = (v2 * premio) / total
tot3 = (v3 * premio) / total
print(f'{tot1:.2f}')
print(f'{tot2:.2f}')
print(f'{tot3:.2f}')