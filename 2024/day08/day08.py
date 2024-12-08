import math
data = [i.strip() for i in open('8.in')]

def dist(a, b):
    return (b[0] - a[0], b[1] - a[1])

def dist2(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    t = math.gcd(dx, dy)
    return (dx / t, dy / t)

def addit(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(n, a):
    return (n * a[0], n * a[1])

grid = {}
for l, line in enumerate(data):
    for c, desc in enumerate(line):
        grid[c, l] = desc

ant = {}
for spot in grid:
    if grid[spot] != '.':
        if grid[spot] not in ant:
            ant[grid[spot]] = [spot]
        else:
            ant[grid[spot]].append(spot)

r = len(data)
an1 = []
an2 = []
for z in ant:
    for i in range(len(ant[z]) - 1):
        for j in range(i + 1, len(ant[z])):
            a, b = ant[z][i], ant[z][j]
            cand = [addit(b, dist(a, b)), addit(a, dist(b, a))]
            for c in cand:
                if 0 <= c[0] < r and 0 <= c[1] < r:
                    an1.append(c)
            for m in range(r):
                cand = [addit(b, mul(m, dist2(a, b))), addit(a, mul(m, dist2(b, a)))]
                for c in cand:
                    if 0 <= c[0] < r and 0 <= c[1] < r:
                        an2.append(c)

print('Answer 1:', len(set(an1)))
print('Answer 2:', len(set(an2)))
