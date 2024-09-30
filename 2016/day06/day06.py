data = [i.strip() for i in open('6.in')]

message1 = ''
message2 = ''
for i in range(len(data[0])):
  s = ''
  for j in range(len(data)):
    s += data[j][i]
  message1 += max(set(s), key = s.count)
  message2 += min(set(s), key = s.count)
print('Answer 1:',message1)
print('Answer 2:',message2)


