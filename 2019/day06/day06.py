data = [x.strip().split(")") for x in open("day6.in")]
orbits = {y : x for x,y in data}

def way(x):
    return (way(orbits[x]) if x in orbits else []) + [x] 

sum = 0

for x in orbits:
    print(x, orbits[x])
    sum += len(way(x)) - 1

print('Answer 1:', sum)

a = (way('SAN'))
b = (way('YOU'))

while a[0] == b[0]:
    a.pop(0)
    b.pop(0)

print('Answer 2:', len(a) + len(b) - 2)
