#AOC Day 3
f = [male.strip() for male in open("AOCDay3.txt" , "r")]

#a-z =  1 - 26 , a = 97
#A-Z = 27 - 52
#A = 65

"""
PART 2
"""
letters = []
tot = 0
while tot < len(f):
    for pc in f[tot]:
            if (pc in f[tot + 1] and pc in f[tot + 2]): #im dumb and should have realized this
                letters.append(pc)
                break
    tot+=3

meth = []
for m in letters:
    for p in m:
        if (p.isupper()):
            mum = ord(p) - 64 + 26
        else:
            mum = ord(p) - 96
        meth.append(mum)        

print(sum(meth))

"""
PART 1
"""
firstHalves = []
secondHalves = []
for pc in f:
    n = list(pc)
    la = int(len(n) / 2)
    frontHalf = n[0:la]
    backHalf = n[la:]
    
    firstHalves.append(frontHalf)
    secondHalves.append(backHalf)

print(firstHalves)

matches = []
for i in range(len(firstHalves)):
    cat = list(set(firstHalves[i]).intersection(secondHalves[i]))
    matches.append(cat)

#this can be a function
convert = []
for m in matches:
    for p in m:
        if (p.isupper()):
            mum = ord(p) - 64 + 26
        else:
            mum = ord(p) - 96
        convert.append(mum)
print(sum(convert))