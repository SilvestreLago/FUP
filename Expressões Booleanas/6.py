x = int(input())
y = int(input())

if (x >= 65 or y >= 30) or (x >= 60 and y >= 25):
    txt = 'Pode se aposentar'
else:
    txt = 'Nao pode se aposentar'

print(txt)