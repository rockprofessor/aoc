data = open('13.in').read().strip().split('\n\n')

ans1 = 0
ans2 = 0
machines = []
for m in data:
    a, b, p = m.split('\n')
    ax = int(a.split()[2][2:-1])
    ay = int(a.split()[3][2:])
    bx = int(b.split()[2][2:-1])
    by = int(b.split()[3][2:])
    p = p.split()[1:]
    px = int(p[0][2:-1])
    py = int(p[1][2:])

    s = (px*by - py*bx) / (ax*by - ay*bx)
    t = (py*ax - px*ay) / (ax*by - ay*bx)

    if t % 1 == 0 and s % 1 == 0 and 0 <= t <= 100 and 0 <= s <= 100:
        ans1 += int(s * 3 + t)

    px += 10000000000000
    py += 10000000000000

    s = (px*by - py*bx) / (ax*by - ay*bx)
    t = (py*ax - px*ay) / (ax*by - ay*bx)

    if t % 1 == 0 and s % 1 == 0 and 0 <= t and 0 <= s:
        ans2 += int(s * 3 + t)

print('Answer 1:', ans1)
print('Answer 2:', ans2)

