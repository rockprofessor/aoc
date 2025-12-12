data = [i.strip() for i in open('11.in')]

graph = {}
for line in data:
    device, out = line.split(': ')
    graph[device] = out.split()

def go(pos):
    if pos == 'out':
        return 1
    s = 0
    for x in graph[pos]:
        s += go(x)
    return s

print('Answer 1:', go('you'))


#svr -> out


def go2(pos, d, f):
    if pos == 'dac':
        a = 1
    elif pos == 'fft':
        b = 1

    elif pos == 'out' and d == 1 and f == 1:
        return 1

    elif pos == 'out' and (d == 0 or f == 0):
        return 0

    s = 0
    for x in graph[pos]:
        s += go2(x, a, b)

print('Answer 2:', go2('svr', 0, 0))
