polymer = open("day05.in").read().strip()

def reduce(data):
    stack = []
    for j in data:
        if stack and j.swapcase() == stack[-1]:
            stack.pop()
        else:
            stack.append(j)
    return stack

print('Answer 1:',len(reduce(polymer)))

records = []

for i in range(ord('a'),ord('z')+1):
    data1 = []
    for j in polymer:
        if j != chr(i) and j != chr(i).upper(): 
            data1.append(j)
    records.append(len(reduce(data1)))

print('Answer 2:',min(records))
