import numpy as np

w = 50
t = 6

strip = []
for i in range(t):
    line = []
    for j in range(w):
        line.append('.')
    strip.append(line)
strip = np.array(strip) 

def print_strip():
    for i in range(t):
        for j in range(w):
            print(strip[i][j], end='')
      print()

def rec(x,y):
    strip[0:y,0:x] = '#'

def xshift(n,i):
    strip[:, n]= np.roll(strip[:, n], i)

def yshift(n,i):
    strip[n, :] = np.roll(strip[n, :], i)


#rect 1x1
#rotate row y=0 by 7

data = [i.strip() for i in open('8.in')]
for x in data:
    com = x.split(' ')
    if com[0] == 'rect':
        a,b = com[1].split('x')
        a = int(a)
        b = int(b)
        rec(a,b)
    else:
        if com[2][0] == 'y':
            yshift(int(com[2][2:]),int(com[4]))
        elif com[2][0] == 'x':
            xshift(int(com[2][2:]),int(com[4]))

print('Answer 1:',np.count_nonzero(strip == '#'))
