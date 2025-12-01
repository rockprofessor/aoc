data = [i.strip() for i in open('1.in')]

p1 = 0
p2 = 0
d = 50

for m in data:
    dir = m[0]
    c = int(m[1:])
    p2 += c // 100
    c %= 100

    if dir == 'R':
        d += c
        if d > 100:
            p2 += 1

    else:
        d_old = d
        d -= c
        if d < 0 and d_old > 0:
            p2 += 1

    d %= 100

    if d == 0:
        p1 += 1

print('Answer 1:', p1)
print('Answer 2:', p1 + p2)
