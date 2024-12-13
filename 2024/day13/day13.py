data = open('13.in').read().strip().split('\n\n')
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
    machines.append([ax, ay, bx, by, px, py])

ans1 = 0
for m in machines:
    ax = m[0]
    ay = m[1]
    bx = m[2]
    by = m[3]
    px = m[4]
    py = m[5]

    s = (px*by - py*bx) / (ax*by - ay*bx)
    t = (py*ax - px*ay) / (ax*by - ay*bx)

    if t % 1 == 0 and s % 1 == 0 and 0 <= t <= 100 and 0 <= s <= 100:
        ans1 += int(s * 3 + t)
print('Answer 1:', ans1)

ans2 = 0
for m in machines:
    ax = m[0]
    ay = m[1]
    bx = m[2]
    by = m[3]
    px = m[4] + 10000000000000
    py = m[5] + 10000000000000

    s = (px*by - py*bx) / (ax*by - ay*bx)
    t = (py*ax - px*ay) / (ax*by - ay*bx)

    if t % 1 == 0 and s % 1 == 0 and 0 <= t and 0 <= s:
        ans2 += int(s * 3 + t)
print('Answer 2:', ans2)

