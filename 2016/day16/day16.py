import copy
a = list('10010000000110000')
a = [int(i) for i in a]
l = 272
l = 35651584  #part 2

while len(a) < l:
    b = copy.deepcopy(a)
    b.reverse()
    for i in range(len(b)):
        if b[i] == 1: b[i] = 0
        else: b[i] = 1 
    a = a + [0] + b
del a[l:]

while len(a)%2 != 1:
    checksum = []
    for i in range(0,len(a)-1,2):
        if a[i] == a[i+1]:
            checksum.append(1)
        else:
            checksum.append(0)
    a = copy.deepcopy(checksum)
  
result = ''
for t in checksum:
    result += str(t)
print('Answer 1:', result)


