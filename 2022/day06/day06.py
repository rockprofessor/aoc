code = open("day6.in").read()

def key(list):
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                return 0
    return 1
i = 0

while i < len(code)-3:
    s = []
    for j in range(i,i+4):
        s.append(code[j])
    if (key(s) == 1):
        print('Answer 1:',i+4)
        i=i+5
        break
    else:
        i=i+1

while i < len(code)-13:
    s = []
    for j in range(i,i+14):
        s.append(code[j])
    if (key(s) == 1):
        print('Answer 1:',i+14)
        i=i+15
        break
    else:
        i = i+1
