data = [i for i in open('1.in')]

p1 = 0
p2 = 0
d = 50

for m in data:
    dr = m[0]
    c = int(m[1:])
    for _ in range(c):
        if dr == 'R':
            d = (d + 1) % 100
        else:
            d = (d - 1) % 100

        if d == 0:
            p2 += 1

    if d == 0:
        p1 += 1

print('Answer 1:', p1)
print('Answer 2:', p2)
