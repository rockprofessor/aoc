data = '278384-824795'
pasmin,pasmax = data.split('-')
pasmin = int(pasmin)
pasmax = int(pasmax)

passlist1 = []

for passcand in range(pasmin,pasmax + 1):
    passcand = str(passcand)
    doublefound = 0        
    rise = 1
    for i in range(0,5):    
        if passcand[i] =  = passcand[i + 1]: doublefound = 1 
        if int(passcand[i])>int(passcand[i + 1]): rise = 0
    if doublefound == 1 and rise == 1:
        passlist1.append(passcand)
print('Answer 1:',len(passlist1))

#answer 2
passlist2 = []

for passcand in range(pasmin,pasmax + 1):
    passcand = str(passcand)
    doublefound = 0        
    rise = 1   
    for i in range(1,4)
        if passcand[i] == passcand[i + 1] and passcand[i] != passcand[i + 2] and passcand[i] != passcand[i-1]: doublefound = 1
    if passcand[4] == passcand[5] and passcand[3] != passcand[5]: doublefound = 1
    if passcand[0] == passcand[1] and passcand[0] != passcand[2]: doublefound = 1
    for i in range(0,5):    
        if int(passcand[i])>int(passcand[i + 1]): rise = 0
    if doublefound == 1 and rise == 1:
        passlist2.append(passcand)
print('Answer 2:',len(passlist2))
