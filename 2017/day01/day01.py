data = open("day1.in").read()
count=0

for i in range(len(data)-1):
    if data[i] == data[i+1]: count += int(data[i])
if data[0] == data[-1]: count += int(data[0])
print('Answer 1:',count)

count=0
for i in range(len(data)):
    if data[i] == data[(i + len(data)//2) % len(data)]: count += int(data[i])

print('Answer 2:',count)
