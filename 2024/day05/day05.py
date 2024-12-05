a, b = open('5.in').read().strip().split('\n\n')

rules = a.split('\n')
updates = b.split('\n')

r = {}
for rule in rules:
    i, j = rule.split('|')
    if int(i) in r:
        r[int(i)].append(int(j))
    else:
        r[int(i)] = [int(j)]

ans1 = 0
ans2 = 0

for update in updates:
    c = True
    up = [int(i) for i in update.split(',')]
    for i in range(len(up) - 1):
        for j in range(i + 1, len(up)):
            if up[i] in r:
                if up[j] not in r[up[i]]:
                    c = False
                    up[i], up[j] = up[j], up[i]

    if c:
        ans1 += up[len(up) // 2]
    else:
        ans2 += up[len(up) // 2]

print('Answer 1:', ans1)
print('Answer 2:', ans2)
