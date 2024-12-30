data = [i.strip() for i in open('11.in')]
R = len(data)

def step():
    for _ in range(1):
        for pos in map:
            map[pos] += 1 

def check():
    for pos in map:
        if map[pos] > 9:
            return True
    return False

def flashcheck():
    for pos in map:
        if map[pos] > 0:
            return False
    return True

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
map = {}

for r, row in enumerate(data):
    for c, col in enumerate(row):
        map[(r,c)] = int(data[r][c])

flash = 0
i = 0
while not flashcheck():
    step()
    while check():
        for pos in map:
            if map[pos] > 9:
                flash += 1
                map[pos] = 0
                for n in range(8):
                    dr, dc = d[n]
                    look = (pos[0] + dr, pos[1] + dc)
                    if look in map:
                        if map[look] > 0:
                            map[look] += 1
    if i == 99:
        print('Answer 1:', flash)
    i += 1
print('Answer 2:', i)


