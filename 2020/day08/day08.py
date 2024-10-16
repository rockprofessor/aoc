file = [i.strip() for i in open('day8.in')]

def testrun(data):
    a = 0     #accumolator
    visit = [0 for i in range(len(data))]
    k = 0
    while visit[k] == 0:
        visit[k] = 1
        words = data[k].split()
        cmd = words[0]
        x = int(words[1])
        if cmd == 'acc': 
            a += x
            k += 1
        if cmd == 'jmp': k += x
        if cmd == 'nop': k += 1
        if k == len(file): 
            print('Answer 2:',a)
            break
    return a
print('Answer 1:',testrun(file))
    
#part 2

for i in range(len(file)):
    if file[i][:3] == 'jmp':
        file[i] = 'nop'+file[i][3:]
        testrun(file)
        file[i] = 'jmp'+file[i][3:]
    if file[i][:3] == 'nop':
        file[i] = 'jmp'+file[i][3:]
        testrun(file)
        file[i] = 'nop'+file[i][3:]
