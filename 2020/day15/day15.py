s = {}

for i, x in enumerate([0, 14, 1, 3, 7]):
    s[x] = i

l = 9   #last number
for i in range(6, int(3e7)):
    if i == 2020: print('Answer 1:', l)
    sl = l  #number before last number

    if l in s:
        l = (i - s[l] - 1)
    else: 
        l = (0)

    s[sl] = i - 1

print('Answer:', l) 
