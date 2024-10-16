import json
data=open('test.in', 'r').read().split('\n\n')

def key_in_list(lst,k):
    if len(lst)!=1: return(0)
    if type(lst[0])==int:
        if k==lst[0]: return(1)
        elif k!=lst[0]: return(0)
    elif type(lst)==list: return(key_in_list(lst[0],k))

def lc(R,S):      #compair two lists R,S
    pos=0
    while True:
        if len(R)==0 and len(S)>0: return(1)
        if len(R)>0 and len(S)==0: return(0)
        if len(R)==0 and len(S)==0: return(2)
        if len(R)<=pos and len(S)>=pos: return(1)
        if len(R)>=pos and len(S)<=pos: return(0)
        if type(R[pos])==int and type(S[pos])==int:
            if R[pos]==S[pos]: 
                if len(R)>pos+1 and len(S)>pos+1: pos+=1
                elif len(R)>pos+1 and len(S)==pos+1: return(0)
                elif len(R)==pos+1 and len(S)>pos+1: return(1)
                else: return(2)
            elif R[pos]<S[pos]: return(1)
            elif R[pos]>S[pos]: return(0)
            else: return(2)
        elif type(R[pos])==list and type(S[pos])==int:
            S[pos]=[S[pos]]
        elif type(R[pos])==int and type(S[pos])==list:
            R[pos]=[R[pos]]
        elif type(R[pos])==list and type(S[pos])==list:
            poslist.append(pos)
            z=lc(R[pos],S[pos])
            if z==1: return(1)   
            elif z==0: return(0)     
            else: pos=poslist.pop()+1


order=[]
index=1
count=0
for set in data:
    poslist=[]
    pair=set.split('\n')
    A=json.loads(pair[0])
    B=json.loads(pair[1])
    order.append(A)
    order.append(B)
    if  lc(A,B)==1: count+=index
    index+=1
print('Answer 1:',count)

order.append([[2]])
order.append([[6]])
help=[]
for i in range(0,len(order)-1):
    for j in range(i+1,len(order)):
        if lc(order[i],order[j])!=1:
            help=order[i]
            order[i]=order[j]
            order[j]=help
f=1
for i,z in enumerate(order):
    print(z)
    if key_in_list(z,6) and len(z)==1: 
        print(i+1)
        f*=i+1
    if key_in_list(z,2) and len(z)==1: f*=i+1


print(f)
#analysed output  [[6]] bring in front ...count
#look at test output
