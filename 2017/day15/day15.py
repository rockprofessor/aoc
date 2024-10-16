# läuft nur in PyCharm
# Replit zu langsam


a = 883
b=  879

#a = 65
#b = 8921

fa = 16807
fb = 48271

d = 2147483647

count = 0

for i in range(int(4E7)):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    anew = bin(a)[-16:]
    bnew = bin(b)[-16:]  
    count += (anew == bnew)
print('Answer 1:', count)

regA = []
regB = []
count2 = 0

while True:
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a % 4 == 0: regA.append(bin(a)[-16:])
    if b % 8 == 0: regB.append(bin(b)[-16:])
    if min(len(regA),len(regB)) > int(5E6): break
        
for i in range(min(len(regA),len(regB))):
    count2 += regA[i] == regB[i]

print('Answer 2:', count2)
