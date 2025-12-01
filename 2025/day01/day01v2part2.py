data = [i.strip() for i in open('1.in')]

p = 0
d = 50

for m in data:
    dir = m[0]
    c = int(m[1:])
    for _ in range(c):
        if dir == 'R':
            d = (d + 1) % 100
        else:
            d = (d - 1) % 100

        if d == 0:
            p += 1

print('Answer 2:', p)
