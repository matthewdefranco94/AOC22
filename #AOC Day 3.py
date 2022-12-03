#AOC Day 3
f = [male.strip() for male in open("AOCDay3.txt" , "r")]

#a-z =  1 - 26 , a = 97
#A-Z = 27 - 52
#A = 65
firstHalves = []
secondHalves = []

for pc in f:
    n = list(pc)
    la = int(len(n) / 2)
    frontHalf = n[0:la]
    backHalf = n[la:]
    
    firstHalves.append(frontHalf)
    secondHalves.append(backHalf)

matches = []
for i in range(len(firstHalves)):
    cat = list(set(firstHalves[i]).intersection(secondHalves[i]))
    matches.append(cat)

convert = []
for m in matches:
    for p in m:
        if (p.isupper()):
            mum = ord(p) - 64 + 26
        else:
            mum = ord(p) - 96
        convert.append(mum)
