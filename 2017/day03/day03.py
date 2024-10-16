data='277678'

max_in_circle=1
edge=1

circle=0
while int(data)>max_in_circle:
    circle+=1
    max_in_circle+=8*circle

z=abs((max_in_circle-int(data))%(2*circle)-circle)
print('Answer 1:',z+circle)

#PART 2

from itertools import count
from collections import defaultdict

data='277678'
snake={}

def mcs(a,b):                 #mcs...make coordinates string
    return(str(a)+' '+str(b))

def getsum(a,b):              #sum of all neighbors
    sum=0
    if mcs(a+1,b) in snake.keys(): sum+=snake.get(mcs(a+1,b))
    if mcs(a-1,b) in snake.keys(): sum+=snake.get(mcs(a-1,b))
    if mcs(a,b+1) in snake.keys(): sum+=snake.get(mcs(a,b+1))
    if mcs(a,b-1) in snake.keys(): sum+=snake.get(mcs(a,b-1))
    if mcs(a+1,b+1) in snake.keys(): sum+=snake.get(mcs(a+1,b+1))
    if mcs(a-1,b-1) in snake.keys(): sum+=snake.get(mcs(a-1,b-1))
    if mcs(a+1,b-1) in snake.keys(): sum+=snake.get(mcs(a+1,b-1))
    if mcs(a-1,b+1) in snake.keys(): sum+=snake.get(mcs(a-1,b+1))
    return(sum)

x=0
y=0
snake[mcs(x,y)]=1
x+=1
snake[mcs(x,y)]=1
limit=0

while limit==0:
    while mcs(x-1,y) in snake.keys() and limit==0:
        y+=1
        snake[mcs(x,y)]=getsum(x,y)
        if getsum(x,y)>int(data): limit=1
    while mcs(x,y-1) in snake.keys() and limit==0:
        x-=1
        snake[mcs(x,y)]=getsum(x,y)
        if getsum(x,y)>int(data): limit=1
    while mcs(x+1,y) in snake.keys() and limit==0:
        y-=1
        snake[mcs(x,y)]=getsum(x,y)
        if getsum(x,y)>int(data): limit=1
    while mcs(x,y+1) in snake.keys() and limit==0:
        x+=1
        snake[mcs(x,y)]=getsum(x,y)
        if getsum(x,y)>int(data): limit=1
print('Answer 2:',getsum(x,y))
