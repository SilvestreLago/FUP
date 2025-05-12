x = int(input())

if (x%5 == 0 and x%3 != 0) or (x%5 != 0 and x%3 == 0):
    val = True

else:
    val = False

print(val)