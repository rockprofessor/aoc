tapedata = [i.strip() for i in open('tape.in')]
data = [i.strip() for i in open('day16.in')]

tape = {}
for item in tapedata:
    part = item.split(' ')
    tape[part[0][: -1]] = int(part[1])

info = {}
for item in data:
    part = item.split()
    aunt = int(part[1][: -1])

    info[aunt]={part[2][: -1]:int(part[3][: -1]),
                part[4][: -1]:int(part[5][: -1]),
                part[6][: -1]:int(part[7])}

for t in tape:
    print(t,tape[t])
print()
print(info[10])

for aunt in info:
    match = 0
    match2 = 0
    for item in info[aunt]:
        if item in ['cats', 'trees'] and info[aunt][item] > tape[item]:
            match2 += 1
        elif item in ['pomeranians', 'goldfish'] and info[aunt][item] < tape[item]:
            match2 += 1
        elif info[aunt][item] == tape[item]:
            match2 += 1


        if info[aunt][item] == tape[item]: 
            match += 1
    if match == 3: print('Answer 1:', aunt)
    if match2 == 3 and match2 != match: print('Answer 2:', aunt)
