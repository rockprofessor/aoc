data = [i for i in open('6.in')]
data2 = open('6.in').read().strip()

instr = data.pop(-1)

data1 = [[int(x) for x in line.split()] for line in data]
instr = instr.split()
calc = {}

for l, line in enumerate(data1):
    for n, numb in enumerate(line):
        if n not in calc:
            calc[n] = []
        calc[n].append(int(numb))

c1 = 0

for n in calc:
    if instr[n] == '+':
        c1 += sum(calc[n])
    else:
        prod = 1
        for c in calc[n]:
            prod *= c
        c1 += prod

print('Answer 1:', c1)

data2 = data2.split('\n')
instr2 = data2.pop(-1)
data2 = [list(i) for i in data2]

for i in range(len(data2[0]) - len(instr2) + 1):
    instr2 = instr2 + ' '

c2 = 0

oper = []
w = []
x = 0
for i in instr2:
    if i != ' ':
        oper.append(i)
        w .append(x)
        x = 0
    else:
        x += 1
w.pop(0)
w.append(x)

while w:
    z = []
    for i in range(w.pop(0)):
        x = []
        for j in range(len(data2)):
            x.append(data2[j].pop(0))
        z.append(int(''.join(x)))
    op = instr.pop(0)

    for i in range(len(data2)):
        if data2[i]:
            data2[i].pop(0)
    if op == '+':
        c2 += sum(z)
    else:
        p = 1
        for h in range(len(z)):
            p *= z[h]
        c2 += p

print('Answer 2:', c2)


