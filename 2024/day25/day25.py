data = open('25.in').read().strip()

data = data.split('\n\n')

keys = []
locks = []
for sch in data:
    s = sch.split('\n')
    if s[0][0] == '#':
        pin = [-1 for _ in range(len(s[0]))]
        for l, line in enumerate(s):
            for i in range(len(line)):
                if line[i] == '.' and pin[i] == -1:
                    pin[i] = l - 1
        locks.append(pin)

    else: 
        pin = [-1 for _ in range(len(s[0]))]
        for l, line in enumerate(s):
            for i in range(len(line)):
                if line[i] == '#' and pin[i] == -1:
                    pin[i] = 6 - l 
        keys.append(pin)

ans = 0
for lock in locks:
    for key in keys:
        ok = True
        for i in range(len(key)):
            if lock[i] + key[i] > 5:
                ok = False
                break
        if ok:
            ans += 1
print('Answer:', ans)
