f = [male.strip() for male in open("AOCDay5.txt" , "r")]


dis = {
    "0" : [],
    "1" : ["H","B","V","W","N","M","L","P"],
    "2" : ["M","Q","H"],
    "3" : ["N","D","B","G","F","Q","M","L"],
    "4" : ["Z","T","F","Q","M","W","G"],
    "5" : ["M","T","H","P"],
    "6" : ["C","B","M","J","D","H","G","T"],
    "7" : ["M","N","B","F","V","R"],
    "8" : ["P","L","H","M","R","G","S"],
    "9" : ["P","D","B","C","N"]
    }

test = {
    "1" : ["N","Z"],
    "2" : ["M" , "C" , "D"],
    "3" : ["P"]
}
move = []
start = []
end = []
for pc in f:
    splits = pc.split(' ')
    numToMove = splits[1]
    startMove = splits[3]
    endMove = splits[-1]
    move.append(numToMove)
    start.append(startMove)
    end.append(endMove)

for m in range(len(start)):
    if (start[m] in dis):
        numBlocks = int(move[m])
        appendingList = dis[str(start[m])]
        recieveList = dis[str(end[m])]
        rewList = []
        for p in range(0,numBlocks):
            rewEle = appendingList.pop()
            rewList.append(rewEle)
        rewList.reverse()
        for r in rewList:
            recieveList.append(r)

    else:
        None
print(dis)


# recieveList = ["M" , "P" , "C"]
# rewList = ['H' , "J" , "L"]
# recieveList = ["M" , "P" , "C" , "'H' , "J" , "L"]
# recieveList.append(rewList) ---> ['M', 'P', 'C', ['H', 'J', 'L']]
# print(recieveList)

# m = 1
# mil = end[-1] , end[-3]
# if (start[m] in dis):
#     newList = dis[str(start[m])]
#     print(newList)

# poop = dis["9"]
# poop.reverse()
# print(poop)