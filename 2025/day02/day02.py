data = open('2.in').read().strip()
ranges = data.split(',')

c1 = 0
c2 = 0

for r in ranges:
    f, l = r.split('-')
    f = int(f)
    l = int(l)
    for x in range (f, l + 1):
        found = []
        t = str(x)

        for i in range(1, len(t)//2 + 1):
            z = t.count(t[:i])
            if z * i == len(t):
                if z == 2:
                    c1 += x
                if x not in found:
                    c2 += x
                    found.append(x)

print('Answer 1:', c1)
print('Answer 2:', c2)
