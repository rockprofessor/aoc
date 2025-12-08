data = [list(map(int, line.split(','))) for line in open('8.in')]

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

distances = []
for i in range(len(data) -1):
    for j in range(i + 1, len(data)):
        distances.append((i, j, dist(data[i], data[j])))

distances = sorted(distances, key=lambda x: x[2])
networks = []

for i in range(5000):
    A = distances[i][0]
    B = distances[i][1]
    found = False
    new = []
    net_temp = []

    while networks:
        look = networks.pop()
        if A in look and B in look:
            new.extend(look)
            found = True

        elif A in look and B not in look:
            look.append(B)
            for l in look:
            new.extend(look)
            found = True

        elif B in look and A not in look:
            look.append(A)
            new.extend(look)
            found = True

        else: net_temp.append(look)

    networks.extend((net_temp))

    if found: networks.append(list(set(new)))
    else: networks.append([A, B])

    if len(networks[0]) == len(data):
        print('Answer 2:', data[A][0] * data[B][0])
        break

    if i == 1000:
        size = [len(n) for n in networks]
        size.sort(reverse = True)
        p = 1
        for z in range(3): p *= size[z]
        print('Answer 1:', p)



