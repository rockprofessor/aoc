data = [i.strip() for i in open('11.in')]

graph = {}
for line in data:
    device, out = line.split(': ')
    graph[device] = out.split()

def go(pos):
    if pos == 'out':
        return 1
    return sum([go(x) for x in graph[pos]])

print('Answer 1:', go('you'))

