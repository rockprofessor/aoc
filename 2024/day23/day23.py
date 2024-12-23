data = [i.strip() for i in open('23.in')]

con = {}
for line in data:
    c1, c2 = line.split('-')
    if c1 not in con: con[c1] = [c2]
    else: con[c1].append(c2)
    if c2 not in con: con[c2] = [c1]
    else: con[c2].append(c1)

found = set()
big =[] 
for c in con:
    count = 0
    b = []
    for i in range(len(con[c]) - 1):
        for j in range(len(con[c])):
            if con[c][i] in con[con[c][j]]:
                b.append(con[c][i])
                found.add(tuple(sorted((c, con[c][i], con[c][j]))))
    if len(big) < len(b) + 1: 
        big = b + [c]

ans1 = 0
for f in list(found):
    check = False
    for n in f:
        if n[0] == 't': check = True
    if check: ans1 += 1

print('Answer 1:', ans1)

big = list(set(big))
ans2 = ','.join(sorted(list(set(big))))
print('Answer 2:', ans2)



