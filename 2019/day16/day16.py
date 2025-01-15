data = open('16.in').read().strip()
data = [[int(i) for i in data]]

pat = [[0 , 1, 0, -1]]
for n in range(len(data[-1])):
    pat.append([x for x in pat[0] for _ in range(n + 2)])

offset = int(''.join(str(i) for i in data[0][:7]))

for _ in range(100):
    new = []
    for n in range(len(data[-1])):
        a = 0
        for i, x in enumerate(data[-1]):
            a += x * pat[n][(i + 1) % (4 * (n + 1))]
        new.append(abs(a) % 10)
    data.append(new)

print('Answer 1:', ''.join(str(i) for i in data[-1][:8]))
