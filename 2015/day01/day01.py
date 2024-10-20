data = open("01.in").read()

print('Answer 1:',data.count('(') - data.count(')'))

floor = 0
for x,c in enumerate(data):
    if c == '(' : floor += 1
    else : floor -= 1
    if floor == -1:
        print('Answer 2:',x+1)
        break
