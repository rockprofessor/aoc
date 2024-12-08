data = [i.strip() for i in open('8.in')]
r = len(data)

def dist(a, b): return (b[0] - a[0], b[1] - a[1])
def addit(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(n, a): return (n * a[0], n * a[1])

grid = {}
ant = {}
for l, line in enumerate(data):
    for c, desc in enumerate(line):
        grid[c, l] = desc
        if desc != '.':
            if desc not in ant:
                ant[desc] = []
            ant[desc].append((c, l))

an1 = set()
an2 = set()

for z in ant:
    for i in range(len(ant[z]) - 1):
        for j in range(i + 1, len(ant[z])):
            a, b = ant[z][i], ant[z][j]
            cand = [addit(b, dist(a, b)), addit(a, dist(b, a))]
            for m in range(r):
                cand = [addit(b, mul(m, dist(a, b))), addit(a, mul(m, dist(b, a)))]
                for c in cand:
                    if 0 <= c[0] < r and 0 <= c[1] < r:
                        if m == 1:
                            an1.add(c)
                        an2.add(c)

print('Answer 1:', len(an1))
print('Answer 2:', len(an2))
