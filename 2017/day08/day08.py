data = [i.strip() for i in open('day8.in')]

reg = {}
for line in data:
    com = line.split()
    if com[0] not in reg: reg[com[0]] = [0]

for line in data:
    com = line.split()
    r = reg[com[0]]
    val = int(com[2])
    
    if com[1] == 'inc' and eval(str(reg[com[4]][-1]) + com[5] + com[6]): r.append(r[-1] + val)
    if com[1] == 'dec' and eval(str(reg[com[4]][-1]) + com[5] + com[6]): r.append(r[-1] - val)
                                                        
maxima1 = []
maxima2 = []
for i in reg:
    maxima1.append(reg[i][-1])
    maxima2.append(max(reg[i]))

print('Answer 1:',max(maxima1))
print('Answer 2:',max(maxima2))
