#AOC Day 4

f = [male.strip() for male in open("AOCDay4.txt" , "r")]

#Ex. 2-8 fully contains 3-7


p1 = 0
p2 = 0

for line in f:
    one,two = line.split(",")
    s1,e1 = one.split("-")
    s2,e2 = two.split('-')
    s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]

    if s1<=s2 and e2<=e1 or s2<=s1 and e1<=e2:
        p1 += 1
    if not (e1 < s2 or e2 < s1):
        p2 += 1


fullyContained = []
for pc in f:
    splits = pc.split(",")
    for sp in splits:
        ffNumb = sp.split("-")
        fullyContained.append(ffNumb)

rangeCount = 0

isInRange = []

for m in range(0 , len(fullyContained), 2):
    if fullyContained[m][0] <= fullyContained[m+1][0] and fullyContained[m+1][1] <= fullyContained[m][1] or fullyContained[m+1][0] <= fullyContained[m][0] and fullyContained[m][1] <= fullyContained[m+1][1]:
        pairs = fullyContained[m] , fullyContained[m+1]
        isInRange.append(pairs)
        rangeCount+=1
    else:
        None
print(len(isInRange))
# print(fullyContained[0][0] , fullyContained[0][1] , fullyContained[2][0] , fullyContained[2][1])
            #[m][0]leftleft , [m+1][0]rightleft
            #[m][1]leftright , [m+1][1]rightright
