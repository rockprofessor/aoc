ranges, ids = open('5.in').read().strip().split('\n\n')

ranges = sorted([tuple(map(int, r.split('-'))) for r in ranges.splitlines()])
ids = list(map(int, ids.splitlines()))

c1 = 0
for i in ids:
    fresh = False
    for r in ranges:
        if r[0] <= i <= r[1]:
            fresh = True
            c1 += 1
            break

print('Answer 1:', c1)

c2 = 0
ref = 0

while ranges: 
    i = max(ref, ranges[0][0])
    r = ranges[0]
    if i <= r[1]:
        c2 += r[1] + 1 - i
        ref = r[1] + 1
    ranges.pop(0)

print('Answer 2:', c2)
