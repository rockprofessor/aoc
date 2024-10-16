with open("day05.in") as f: formular = f.read()
data1=list(formular)

def react(data):
    len1=len(data)+1
    while len(data)<len1:
        len1=len(data)
        i=0
        while i<len(data)-1:
            if (ord(data[i])==(ord(data[i+1])+32)) or (ord(data[i])==(ord(data[i+1])-32)): 
                #del data[i:i+1]
                data.pop(i)
                data.pop(i)
                i-=1
            i+=1  
    return(len(data))

print('Answer 1:',react(data1))

for j in range(ord('a'),ord('d')):
    data2=list(formular)
    len2=len(data2)+1
    while len(data2)<len2:
        len2=len(data2)
        i=0
        while i<len(data2)-1:
            if ord(data2[i])>96: 
                if ord(data2[i])==j and ord(data2[i+1])==j-32: 
                    data2.pop(i)
                    data2.pop(i)
                    i-=1
                i+=1  

            else: 
                if ord(data2[i])==j-32 and ord(data2[i+1])==j: 
                    data2.pop(i)
                    data2.pop(i)
                    i-=1
                i+=1  

    print(chr(j),react(data2))
