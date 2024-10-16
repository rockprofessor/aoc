data = open('day7.in').read().split(',')
for i in range(len(data)): 
  data[i] = int(data[i])

data.sort()
m = len(data) // 2

sum = 0
for j in data:
  sum += abs(j-data[m])

print('Answer 1:',sum)

n = max(data)
s = []
for i in range(n):
  sum = 0
  for j in data:
    r = abs(j-i)
    sum += (r+1)*r/2
  s.append(sum)

print('Answer 2:',int(min(s)))
