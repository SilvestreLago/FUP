sec = int(input())
h = sec // 3600
min = (sec % 3600) // 60
sec = sec % 60
print(h)
print(min)
print(sec)