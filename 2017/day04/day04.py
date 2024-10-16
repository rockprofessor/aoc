data=[i.strip() for i in open('day4.in')]

#data=['abcde fghij','abcde xyz ecdab','a ab abc abd abf abj','iiii oiii ooii oooi oooo','oiii ioii iioi iiio']

countvalid=0
for line in data:
    words=line.strip().split()
    if len(words)==len(set(words)):
        countvalid+=1
print('Answer 1:',countvalid)

count=0
for line in data:
    words=line.strip().split()
    isanna=0
    for i in range(0,len(words)-1):
        for j in range(i+1,len(words)):
            if sorted(words[i])==sorted(words[j]):
                isanna=1
    if isanna==0: count+=1
print('Answer 2:',count)
