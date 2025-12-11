import math

# (col, row)
data = [tuple(int(x.strip()) for x in line.split(',')) for line in open('t.in')]
grid = []

area_max = 0
for i in range(len(data) - 1):
    for j in range(len(data)):
        area = (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1)
        if area > area_max:
            area_max = area

print('Answer 1:', area_max)

area_max = 0
areas = []
edges = []

for i in range(len(data) - 1):
    for j in range(len(data)):
        area = (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1)
        a = min(data[i][0], data[j][0]) # col min
        b = min(data[i][1], data[j][1]) # row min
        c = max(data[i][0], data[j][0]) # col max
        d = max(data[i][1], data[j][1]) # row max
        if a != c and b != d:
            areas.append(((a, b), (c, d), area))

data.append(data[0])

for i in range(len(data) - 1):
    (a, b) = data[i]
    (c, d) = data[i + 1]
    edges.append(((a, b), (c, d)))

areas = list(set(areas))
areas = sorted(areas, key = lambda x: x[2], reverse = True)

edges = list(set(edges))
edges = sorted(edges, key = lambda p: math.dist(p[0], p[1]), reverse = True)

def cross(e, f, g, h):
    for edge in edges:
        continue

for area in areas:
    for edge in edges:

        continue

print('Answer 2:', area_max)
