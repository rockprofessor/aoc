import copy
import itertools

data = [i.strip() for i in open('t.in')]
data = [int(i) for i in data]

t = sum(data)//3

data.sort(reverse=True)
test = copy.deepcopy(data)

sum = 0 
for i in test:
  print(i)
  
  if sum + i < t:
    print('found')
    sum += i
  print(sum)

print(sum)
  
  


