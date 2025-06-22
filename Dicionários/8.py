import math
coordXY = {}
coordRA = {}
coordRA['r'] = float(input())
coordRA['a'] = float(input())
coordXY['x'] = coordRA['r'] * math.cos(coordRA['a'])
coordXY['y'] = coordRA['r'] * math.sin(coordRA['a'])
print(coordRA)
print(coordXY)