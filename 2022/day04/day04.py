data = [i.strip() for i in open('day4.in')]

score1 = 0
score2 = 0
for x in data:
    a,b = x.split(',')
    u1,u2 = a.split('-')
    v1,v2 = b.split('-')
    u1,u2,v1,v2 = [int(x) for x in [u1,u2,v1,v2]]

    if (u1 <= v1 and v2 <= u2) or (v1 <= u1 and u2 <= v2):
        score1 += 1
    if not(u2 < v1 or v2 < u1):
        score2 += 1
print('Answer 1:',score1)
print('Answer 2:',score2)
