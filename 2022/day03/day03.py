data=[i.strip() for i in open('test.in')]

sum1 = 0
sum2=0
group = []

for x in data:
    a = list(x[:(len(x)//2)])
    b = list(x[(len(x)//2):])
    group.append(list(x))
    for c in a:
        if c in b:
            if ord(c)>96: sum1 += ord(c)-96
            else: sum1 += ord(c)-38
            break
    if len(group) == 3:
        for c in group[0]:
            if c in group[1] and c in group[2]:
                if ord(c)>96: sum2 += ord(c)-96
                else: sum2 += ord(c)-38
                break
        group = []

print('Answer 1:',sum1)
print('Answer 2:',sum2)
