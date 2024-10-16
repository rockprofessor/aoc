data=open('day4.in').read().strip().split('\n')
i=0
count=0
while i<len(data):
    words=[]
    passinfo=''
    while data[i]!='':
        words=data[i].split(' ')
        for r in words:
            passinfo+=r+' '
        if i<len(data)-1: i+=1
        else: break
    byr=0
    iyr=0
    eyr=0
    hgt=0
    hcl=0
    ecl=0
    pid=0
    cid=0
    info=passinfo.split(' ')
    
    for z in info:
        if z!='': 
            a,b=z.split(':')
            if a=='byr' : byr=int(b)
            if a=='iyr' : iyr=int(b)
            if a=='eyr' : eyr=b
            if a=='hgt' : hgt=b
            if a=='hcl' : hcl=b
            if a=='ecl' : ecl=b
            if a=='pid' : pid=b  
            if a=='cid' : cid=b
    if byr!=0 and iyr!=0 and hgt!=0 and hcl!=0 and ecl!=0 and pid!=0 and eyr!=0 : 
        count+=1
    i+=1

print('Answer 1:',count)

#part 2------------------
eyecolour=['amb','blu','brn','gry','grn','hzl','oth']
i=0
count=0
while i<len(data):
    words=[]
    passinfo=''
    while data[i]!='':
        words=data[i].split(' ')
        for r in words:
            passinfo+=r+' '
        if i<len(data)-1: i+=1
        else: break
    byr=0
    iyr=0
    eyr=0
    hgt=0
    hcl=0
    ecl=0
    pid=0
    cid=0
    info=passinfo.split(' ')
    
    for z in info:
        if z!='': 
            a,b=z.split(':')
            if a=='byr' and len(b)==4 and 1920<=int(b)<=2002: byr=1
            if a=='iyr' and len(b)==4 and 2010<=int(b)<=2020: iyr=1
            if a=='eyr' and len(b)==4 and 2020<=int(b)<=2030: eyr=1
            if a=='hgt' : 
                u=b[:-2]
                v=b[-2:]
                if (v=='cm' and 150<=int(u)<=193): hgt=1
                if (v=='in' and 59<=int(u)<=76): hgt=1
            if a=='hcl' and b[0]=='#' and len(b)==7: hcl=1
            if a=='ecl' and b in eyecolour: ecl=1
            if a=='pid' and len(b)==9: pid=1
    if byr!=0 and iyr!=0 and hgt!=0 and hcl!=0 and ecl!=0 and pid!=0 and eyr!=0 : 
        count+=1
    i+=1

print('Answer 2:',count)


