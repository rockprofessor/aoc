count=0
with open('day3.in') as file:  
    for line in file:       
        a,b,c=line.split()   
        a=int(a)
        b=int(b)
        c=int(c)
        if (a+b)>c and (a+c)>b and (b+c)>a:
          count+=1       
print('Answer 1:',count)

data=[]
with open('day3.in') as file:  
    for line in file:       
        data.append(line.split())

count=0
for i in range(0,len(data),3):
  for j in range(3):
    a=int(data[i][j])
    b=int(data[i+1][j])
    c=int(data[i+2][j])
    if (a+b)>c and (a+c)>b and (b+c)>a:
      count+=1       
print('Answer 2:',count)
    
  



