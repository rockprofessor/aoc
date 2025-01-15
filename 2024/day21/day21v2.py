from functools import lru_cache
data = [i.strip() for i in open('t.in')]

numpad = {'7': (0, 0), '8': (1, 0), '9': (2, 0),
          '4': (0, 1), '5': (1, 1), '6': (2, 1),
          '1': (0, 2), '2': (1, 2), '3': (2, 2),
          'A': (2, 3), '0': (1, 3)}

dirpad = {'^': (1, 0), 'A': (2, 0),
          '<': (0, 1), 'v': (1, 1), '>': (2, 1)}

def m1(pos, togo):
    type1 = ''
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
    print(type1)
    return type1

@lru_cache(maxsize=None)
def m2(type1):
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
            if dx > 0: type2 += '>' * dx
            if dy < 0: type2 += '^' * - dy
            if dy > 0: type2 += 'v' * dy
        type2 += 'A'
        pos = togo
    print(type2)
    return type2

ans1 = ans2 = 0
#for line in data:
#    type1 = m1(line)
#    for i in range(2):
#        type1 = m2(type1)
#    ans1 += len(type1) * int(line[:-1])
#print('Answer 1:', ans1)

for line in data:
    for i in range(len(line) - 1):
        print(line[i], line[i + 1])
        type1 = m1(line[i], line[i + 1])
        for i in range(2):
            type1 = m2(type1)
        print(len(type1))
        ans2 += len(type1)
    ans2 *= int(line[:-1])
print('Answer 2:', ans2)
