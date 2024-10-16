data = open('day6.in').read().split(',')
for i in range(len(data)): data[i] = int(data[i])

def fishcount(days):
    counter=[]
    for j in range(9):
        counter.append(0)
        counter[j]=data.count(j)
    for k in range(days):
        x=counter.pop(0)
        counter[6]+=x
        counter.append(x)
    return sum(counter)
 
print('Answer 1:',fishcount(80))
print('Answer 2:',fishcount(256))
