data = open('t.in').read().strip()

m = 0
disk = []
for i in data:
   for j in range(int(i)):
       if m % 2 == 0:
          disk.append(m//2)
       else:
          disk.append('.')
   m += 1

while '.' in disk:
    disk[disk.index('.')] = disk.pop(-1)

ans1 = 0
for i in range(len(disk)):
    ans1 += i * int(disk[i])
print('Answer 1:', ans1)

# part 2
#        fid  startpos  length
# files: {0:   (0,        2),       1: (5, 3),       2: (11, 1),        3: (15, 3)}
# spaces:                [(2, 3),          (8, 3),           (12, 3)]
#                   startpos length

files = {}
free =[]
fid = 0
p = 0
for i, x in enumerate(data):
    x = int(x)
    if i % 2 == 0:
        files[fid] = (p, x)
        fid += 1
    else:
        if x != 0:
            free.append((p, x))
    p += x
print(files)
print(free)
while fid > 0:
    fid -= 1
    p1, s1 = files[fid]
    for i, (p2, s2) in enumerate(free):
        if p2 < p1 and s1 <= s2:
            files[fid] = (p2, s1)
            if s1 == s2:
                free.pop(i)
            else:
                free[i] = (p2 + s1, s2 - s1)
            break
ans2 = 0
for fid, (p, s) in files.items():
    for x in range(p, p + s):
        ans2 += fid * x

print('Answer 2:', ans2)
