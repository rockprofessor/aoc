data = [i.strip() for i in open('day14.in')]

info = {}
for i in data:
  word = i.split(' ')
  info[word[0]]=[int(word[3]),int(word[6]),int(word[13]),0]

#info[name,v,go time, rest time, way]

t = 2503
#t = 1000
traveld = []
for name in info:
  v = info[name][0]
  go = info[name][1]
  rest = info[name][2]
  way = v*go*(t//(go+rest))
  if t%(go+rest) >= go: 
    way += v*go
  else: 
    way += v*t%(go+rest)
  traveld.append(way)
  
print('Answer 1:',max(traveld))

#part 2 in sec steps
traveld = [0 for i in range(len(info))]
score = [0 for i in range(len(info))]
for step in range(1,t+1):
  for n,name in enumerate(info):
    v = info[name][0]
    go = info[name][1]
    rest = info[name][2]
    if step%(go+rest) <= go and step%(go+rest): traveld[n] += v
  best = max(traveld)

  for i in range(len(traveld)):
    if traveld[i] == best: score[i] += 1

print('Answer 2:',max(score)) 
