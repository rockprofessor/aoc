import math

# (col, row)
data = [tuple(int(x.strip()) for x in line.split(',')) for line in open('9.in')]
grid = []

area_max = 0
for i in range(len(data) - 1):
    for j in range(len(data)):
        area = (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1)
        if area > area_max:
            area_max = area

print('Answer 1:', area_max)

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

def edge_sort(edge):
    p1, p2 = edge
    if p1[0] > p2[0] or (p1[0] == p2[0] and p1[1] > p2[1]):
        return (p2, p1)
    return (p1, p2)

edges = list(set(edges))
edges = [edge_sort(e) for e in edges]
edges = sorted(edges, key = lambda p: math.dist(p[0], p[1]), reverse = True)

for ((a, b), (c, d), area) in areas:
    go = True
    for (x, y) in data:
        if a < x < c and b < y < d:
            go = False
            break
    go2 = True
    if go:
        for ((e, f), (g, h)) in edges:
            if e == g:
                if a < e < c and f <= b and h >= d:
                    go2 = False
            else:
                if b < f < d and e <= a and g >= c:
                    go2 = False
        if go2:
            print('Answer 2:', ((a, b), (c, d), area))
            break

