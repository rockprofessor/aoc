from collections import OrderedDict

def rem_dup(s): 
        return "".join(OrderedDict.fromkeys(s))

data = [i.strip() for i in open('day6.in')]
#last line in in file must be empty!!!!

sum1 = 0
sum2 = 0
group = ''
mem = 0
for line in data:
    if line:
        group += line
        mem += 1
    else:
        sum1 += len(rem_dup(group))
        for c in rem_dup(group):
            if group.count(c) == mem:
                sum2 += 1
        group = ''
        mem = 0
print('Answer 1:', sum1)
print('Answer 2:', sum2)
