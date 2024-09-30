#from collections import defaultdict

data=[i.strip() for i in open('day4.in')]
idsum=0
for line in data:
  name=''
  cl={} #lettercount
  a,id,chksum=line[:-11],line[-10:-7],line[-6:-1]
  r=a.split('-')
  for i in r: name+=i
  #print(name,id,chksum)
  for i in name: cl[i]=name.count(i)
  g=list(cl.keys())
  h=list(cl.values())
  check=''
  for z in range(5):
    #print(max(h),g[h.index(max(h))])
    if h.count(max(h))==1:
      check+=g[h.index(max(h))]
      del g[h.index(max(h))]
      del h[h.index(max(h))]
    else:
      l=[]
      for u in range(h.count(max(h))):
        l.append(g[h.index(max(h))])
        del g[h.index(max(h))]
        del h[h.index(max(h))]
      l=sorted(l)
      check+=''.join(l)
    if len(g)==0:break
  if check[:5]==chksum: idsum+=int(id)
print('Answer 1:',idsum)

#part2--------------------

for line in data:
  cryp,id=line[:-11],line[-10:-7]
  id=int(id)

  for j in range(id):
    real=''
    for i in cryp:
      if ord('a')<=ord(i)<ord('z'): real+=chr(ord(i)+1)
      if ord(i)==ord('z'): real+='a'
      if i=='-': real+=(' ')
      if i==' ': real+=(' ')
    cryp=real
    
  if real=='northpole object storage': print('Answer 2:',id)


