import hashlib
key='iwrupvqb'
found=0
i=0

while found==0:
    data=key+str(i)
    result=hashlib.md5(data.encode())
    if result.hexdigest()[:5]=='00000':
        print('Answer 1:',i)
        found=1
    i+=1

#part 2-------------
found=0
i=0

while found==0:
    data=key+str(i)
    result=hashlib.md5(data.encode())
    if result.hexdigest()[:6]=='000000':
        print('Answer 2:',i)
        found=1
    i+=1
