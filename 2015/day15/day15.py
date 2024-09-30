import numpy as np
data = [i.strip() for i in open('day15.in')]
ing = []
for i in data:
  part = i.split(' ')
  cap = int(part[2][:-1])
  dur = int(part[4][:-1])
  fla = int(part[6][:-1])
  tex = int(part[8][:-1])
  cal = int(part[10])
  ing.append([cap,dur,fla,tex,cal])
ing = np.array(ing)

print(ing)

best = 0
best2 = 0
for a in range(1,98):
  for b in range(1,100-a):
    for c in range(1,100-a-b):
      d = 100-(a+b+c) 
      prod = 1
      erg = a * ing[0] + b * ing[1] + c * ing[2] + d * ing[3]  
      for i in range(len(erg)-1):
        if erg[i] > 0:
          prod *= erg[i]
        else: prod = 0
      #print(a,b,c,d,prod) 
      if prod > best: best = prod
      if erg[4] == 500 and prod > best2: best2 = prod
print('Answer 1:',best)
print('Answer 2:',best2)
