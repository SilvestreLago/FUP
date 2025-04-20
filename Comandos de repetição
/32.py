x = input()
frase = ''
for c in x:
    val = ord(c)+1
    frase += chr(val)
print(frase)