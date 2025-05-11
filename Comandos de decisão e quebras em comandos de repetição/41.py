x = input()
tam = len(x)
txt = ""
for c in range(tam):
    if x[c] == "0":
        txt += "1"
    else:
        txt += x[c]
print(txt)