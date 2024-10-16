data=[i.strip() for i in open('day1.in')]

for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if int(data[i])+int(data[j])==2020:
            print('Answer 1:',int(data[i])*int(data[j]))

for i in range(len(data)-2):
    for j in range(i+1,len(data)-1):
        for k in range(i+2,len(data)):
            if int(data[i])+int(data[j])+int(data[k])==2020:
                print('Answer 2:',int(data[i])*int(data[j])*int(data[k]))
