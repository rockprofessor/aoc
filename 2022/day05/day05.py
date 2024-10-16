import copy
lines = [i.strip() for i in open('day5.in')]

#zähle max Turmhöhe r-1
r = 0
while lines[r] != '': r += 1

#stapel1...liste mit Türmen aus Angabe für task 1
stapel1 = []
for i in range(1,len(lines[0]),4):
    s = []
    for n in range(r-2,-1,-1):
        if lines[n][i] != ' ':
            s.append(lines[n][i])
    stapel1.append(s)

#stapel2...liste mit Türmen aus Angabe für task 2
#beachte deep copy vs shallow copy
stapel2=copy.deepcopy(stapel1)
#umbauanweisungen entschlüsseln
#m...Anzahl der zu bewegenden blöcke
#s...von Turm
#t...nach turm
for i in range(r+1,len(lines)):
    a,b = lines[i].split(' from ')
    c,m = a.split('move ')
    s,t = b.split(' to ')
    s = int(s)-1
    t = int(t)-1
    m = int(m)
    u = []    #zwischenliste wegen umgekehrter Reihenfolge
    for z in range(0,m):    #moves task 1
        stapel1[t].append(stapel1[s].pop())
        u.append(stapel2[s].pop())
    for z in range(0,m):
        stapel2[t].append(u.pop())
    i += 1

ans1 = ''
ans2 = ''
for i in range(0,r):
    ans1 += stapel1[i].pop()
    ans2 += stapel2[i].pop()
print('Answer 1:',ans1)
print('Answer 2:',ans2)
