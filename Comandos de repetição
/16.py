x = 1
y = 1
s = 0
for c in range(50):
    s += x / y
    x += 2
    y += 1
print(f"{s:.10f}")