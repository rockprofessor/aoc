data = open('15.in').read().strip()
warehouse, movements = data.split('\n\n')
warehouse = warehouse.split('\n')
movements = movements.replace('\n', '')

walls = set()
boxes = set()

def ac(a, b):
    return (a[0] + b[0], a[1] + b[1])

D = ((0, 1), (0, -1), (1, 0), (-1, 0))
M = (  '>',    '<',     'v',     '^')

warehousewide = []
for r, row in enumerate(warehouse):
    line = ''
    for c, x in enumerate(row):
        if x == '.':
            line += '..'
        if x   == '#':
            walls.add((r, c))
            line += '##'
        elif x == 'O':
            boxes.add((r, c))
            line += '[]'
        elif x == '@':
            pos = (r, c)
            line += '@.'
    warehousewide.append(line)

for m in movements:
    step = D[M.index(m)]
    next = ac(pos,  step)
    if next in walls:
        continue
    elif next not in boxes:
        pos = next
    else:
        while next in boxes:
            next = ac(next, step)
        if next in walls:
            continue
        pos = ac(pos, step)
        boxes.remove(pos)
        boxes.add(next)

ans1 = 0
for box in boxes:
    ans1 += 100 * box[0] + box[1]

print('Answer 1:', ans1)

walls = set()
leftboxes = []
rightboxes = []
for r, row in enumerate(warehousewide):
    for c, x in enumerate(row):
        if x   == '#': walls.add((r, c))
        elif x == '[': leftboxes.append((r, c))
        elif x == ']': rightboxes.append((r, c))
        elif x == '@': pos = (r, c)

def prwh():
    for r in range(len(warehousewide)):
        line = ''
        for c in range(len(warehousewide[0])):
            if (r, c) in walls: line += '#'
            elif (r, c) in leftboxes: line += '['
            elif (r, c) in rightboxes: line += ']'
            elif (r, c) == pos: line += '@'
            else: line += '.'
        print(line)

for m in movements:
    d = D[M.index(m)]
    next = ac(pos, d)
    if next in walls:
        continue
    elif next not in leftboxes and next not in rightboxes:
        pos = next
    else:
        moveleft = []
        moveright = []
        if d[0] == 0:   #push left or right
            if d[1] == 1:   #push right
                while next in leftboxes:
                    moveleft.append(next)
                    moveright.append(ac(next, d))
                    next = ac(ac(next, d), d)
                if next not in walls:
                    pos = ac(pos, d)
                    for l in moveleft:
                        leftboxes.remove(l)
                        leftboxes.append(ac(l, d))
                    for r in moveright:
                        rightboxes.remove(r)
                        rightboxes.append(ac(r, d))
            else:           #push left
                while next in rightboxes:
                    moveright.append(next)
                    moveleft.append(ac(next, d))
                    next = ac(ac(next, d), d)
                if next not in walls:
                    pos = ac(pos, d)
                    for l in moveleft:
                        leftboxes.remove(l)
                        leftboxes.append(ac(l, d))
                    for r in moveright:
                        rightboxes.remove(r)
                        rightboxes.append(ac(r, d))

        else:   #push up or down
            next = ac(pos, d)
            if next not in rightboxes and next not in leftboxes and next not in walls:
                pos = next
            elif next in walls:
                continue
            else:
                tomove = []
                go = True
                if next in leftboxes:
                    front = [next]
                if next in rightboxes:
                    front = [ac(next, (0, -1))]
                while front and go:
                    f = front.pop(0)
                    if f in walls:
                        go = False
                    if f in leftboxes:
                        front.append(ac(f, d))
                        tomove.append(f)
                    elif f in rightboxes:
                        front.append(ac(ac(f, d), (0, -1)))
                        tomove.append(ac(f, (0, -1)))
                    f = ac(f, (0, 1))
                    if f in walls:
                        go = False
                    if f in leftboxes:
                        front.append(ac(f, d))
                        tomove.append(f)
                    elif f in rightboxes:
                        front.append(ac(ac(f, d), (0, -1)))
                        tomove.append(ac(f, (0, -1)))

                if go:
                    tomove = list(set(tomove))
                    while tomove:
                        t = tomove.pop(-1)
                        leftboxes.remove(t)
                        leftboxes.append(ac(t, d))
                        rightboxes.remove(ac(t, (0, 1)))
                        rightboxes.append(ac(ac(t, (0, 1)), d))
                    pos = next

ans2 = 0
for l in leftboxes:
    ans2 += l[0] * 100 + l[1]
print('Answer 2:', ans2)
