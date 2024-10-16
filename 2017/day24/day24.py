data = [i.strip() for i in open('day25.in')]

state = data.pop(0)[-2:-1]
steps = int(data.pop(0).split()[-2])
data.pop(0)

bp = {}
for i in range(0,len(data),10):
    state = data[i][-2:-1]
    zero = data[i+2:i+5]
    one = data[i+6:i+9]
    bp[state]=[[int(zero[0][-2:-1]),zero[1].split(' ')[-1][:-1],zero[2].split(' ')[-1][:-1]],
                         [int(one[0][-2:-1]),one[1].split(' ')[-1][:-1],one[2].split(' ')[-1][:-1]]]

tape =[0 for i in range(10000)]
cursor = 5000

for i in range(steps):
    curr = tape[cursor]
    tape[cursor] = bp[state][curr][0]
    if bp[state][curr][1] == 'right': cursor += 1
    else: cursor -= 1
    state = bp[state][curr][2]
    
print('Answer 1:', sum(tape))
print('No Answer 2 task!')
