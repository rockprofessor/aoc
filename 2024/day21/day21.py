from functools import lru_cache
data = [i.strip() for i in open('t.in')]

numpad = {'7': (0, 0), '8': (1, 0), '9': (2, 0),
          '4': (0, 1), '5': (1, 1), '6': (2, 1),
          '1': (0, 2), '2': (1, 2), '3': (2, 2),
          'A': (2, 3), '0': (1, 3)}

dirpad = {'^': (1, 0), 'A': (2, 0),
          '<': (0, 1), 'v': (1, 1), '>': (2, 1)}


def m1(line):
    pos = 'A' 
    type1 = ''
    for togo in line:
        dx = numpad[togo][0] - numpad[pos][0] 
        dy = numpad[togo][1] - numpad[pos][1]
        if numpad[pos][1] == 3 and numpad[pos][0] + dx == 0:
            if dy < 0: type1 += '^' * - dy
            if dx < 0: type1 += '<' * - dx
        elif numpad[pos][0] == 0 and numpad[pos][1] + dy == 3:
            if dx > 0: type1 += '>' * dx
            if dy > 0: type1 += 'v' * dy
        else: 
            if dx < 0: type1 += '<' * - dx
            if dy < 0: type1 += '^' * - dy
            if dy > 0: type1 += 'v' * dy
            if dx > 0: type1 += '>' * dx
        type1 += 'A'
        pos = togo
    return type1

def m2(type1, n):
    if n == 0: 
        return type1
    pos = 'A'
    type2 = '' 
    for togo in type1:
        dx = dirpad[togo][0] - dirpad[pos][0] 
        dy = dirpad[togo][1] - dirpad[pos][1]
        if dirpad[pos][1] == 0 and dirpad[pos][0] + dx == 0:
            if dy > 0: type2 += 'v' * dy
            if dx < 0: type2 += '<' * - dx
        elif dirpad[pos][0] == 0 and dirpad[pos][1] + dy == 0:
            if dx > 0: type2 += '>' * dx
            if dy < 0: type2 += '^' * - dy
        else:
            if dx < 0: type2 += '<' * - dx
            if dy > 0: type2 += 'v' * dy
            if dy < 0: type2 += '^' * - dy
            if dx > 0: type2 += '>' * dx
        type2 += 'A'
        pos = togo
    return m2(type2, n - 1)

def m3(pos, togo):
    type2 = ''
    dx = dirpad[togo][0] - dirpad[pos][0] 
    dy = dirpad[togo][1] - dirpad[pos][1]
    if dirpad[pos][1] == 0 and dirpad[pos][0] + dx == 0:
        if dy > 0: type2 += 'v' * dy
        if dx < 0: type2 += '<' * - dx
    elif dirpad[pos][0] == 0 and dirpad[pos][1] + dy == 0:
        if dx > 0: type2 += '>' * dx
        if dy < 0: type2 += '^' * - dy
    else:
        if dx < 0: type2 += '<' * - dx
        if dy > 0: type2 += 'v' * dy
        if dy < 0: type2 += '^' * - dy
        if dx > 0: type2 += '>' * dx
    return type2 + 'A' 

@lru_cache(maxsize=None)
def m4(pos, togo, n):
    if n == 1:
        return move[(pos, togo)]
    a = 'A' + move[(pos, togo)]
    b = 'A'
    for i in range(len(a) - 1):
        b += m4(a[i], a[i + 1], n - 1)
    return b

buttons = list(dirpad.keys())
move = {}
for i in range(len(buttons)):
    for j in range(len(buttons)):
        move[(buttons[i], buttons[j])] = m3(buttons[i], buttons[j])

ans1 = ans2 = 0
for line in data:
    out1 = m1(line)
    out2 = m2(out1, 2)
    ans1 += len(out2) * int(line[:-1])
print('Answer 1:', ans1)


print(len(m4('A', '<', 8)) - 1)
