data = [i.strip() for i in open('12.in')]
R = len(data)

for line in data:
    print(line)
print()

def look(p):
    dirlook = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen = []
    for d in dirlook:
        new = (p[0] + d[0], p[1] + d[1]) 
        if new in garden:
            if garden[new] == garden[p]:
                seen.append(new)
    return seen

def lb(p):
    dirlook = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen = []
    for d in dirlook:
        new = (p[0] + d[0], p[1] + d[1]) 
        if new in garden:
            if garden[new] != garden[p]:
                seen.append((p[0] + d[0]*(0.5), p[1] + d[1]*0.5))
    return seen

def bor(p):
    dirlook = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    bor = []
    for d in dirlook:
        new = (p[0] + d[0], p[1] + d[1]) 
        if new not in garden:
            bor.append((p[0] + d[0]*(0.5), p[1] + d[1]*0.5))
    return bor

grid = []
garden = {}
for r in range(R):
    for c in range(R):
        garden[(r, c)] = data[r][c]
        grid.append((r, c))
regions = []

while grid:
    totest = grid.pop(0)
    reg =[totest]
    curr = [totest]
    newcurr = []
    while curr:
        c = curr.pop()
        for l in look(c):
            if l not in reg and l not in newcurr and l not in curr:
                newcurr.append(l)
                reg.append(l)
                grid.remove(l)
        for nc in newcurr:
            curr.append(nc)
        newcurr = []
    regions.append(reg)

ans1 = 0
ans2 = 0
for r in regions:
    verbor = {}
    horbor = {}
    border = set()
    fence = 0
    for cand in r:
        fence += 4 - len(look(cand))
        nb = []
        for l in lb(cand):
            border.add(l)
        fence += len(nb)
        for b in bor(cand):
            border.add(b)

    ans1 += fence * len(r)
    for b in border:
        if int(b[1] * 10) % 10 == 5:
            if b[1] in verbor:
                verbor[b[1]].append(b[0])
            else:
                verbor[b[1]] = [b[0]]
        else:
            if b[0] in horbor:
                horbor[b[0]].append(b[1])
            else:
                horbor[b[0]] = [b[1]]

    count = 0
    for h in horbor:
        horbor[h].sort()
        count += 1
        for i in range(0, len(horbor[h]) - 1):
            if horbor[h][i] != horbor[h][i + 1] - 1:
                count += 1
            else:
                if (horbor[h][i] + horbor[h][i + 1]) / 2 in verbor: 
                    if h-0.5 in verbor[(horbor[h][i] + horbor[h][i + 1]) / 2]:
                        if h+0.5 in verbor[(horbor[h][i] + horbor[h][i + 1]) / 2]:
                            count += 2

    for v in verbor:
        verbor[v].sort()
        count += 1
        for i in range(0, len(verbor[v]) - 1):
            if verbor[v][i] != verbor[v][i + 1] - 1:
                count += 1
    ans2 += count * len(r) 
    for h in horbor:
        print('h:', h, horbor[h])
    for v in verbor:
        print('v:', v, verbor[v])

    print(data[r[0][0]][r[0][1]],'area:', len(r), 'fence:', count,'totoal:', count * len(r))
    print()
print()
print('Answer 1:', ans1)
print('Answer 2:', ans2)



