data = [i.strip() for i in open('day1.in')]
data = [int(i) for i in data]

m = data[0]
count = 0
for i in data:
    if i > m:
        count += 1
    m = i
print('Answer 1:',count)

#part 2 ********************
s = []

for i in range(len(data)-2):
    s.append(data[i]+data[i+1]+data[i+2])

m = data[0]
count = 0
for i in s:
    if i > m:
        count += 1
    m = i
print('Answer 2:',count)
