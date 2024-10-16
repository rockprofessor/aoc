import copy
data = [i.strip() for i in open('day20.in')]
for t in range(len(data)):
    data[t] = int(data[t])

input = copy.deepcopy(data)



for i in data:
    if i: 
        ind = input.index(i)

        if (i+ind):
            input.insert((i+ind)%len(input),i)
        else: input.append(i)
        input.pop(ind)

mark = input.index(0)
print('Answer 1:',input[(mark+1000)%len(input)]+input[(mark+2000)%len(input)]+input[(mark+3000)%len(input)])
